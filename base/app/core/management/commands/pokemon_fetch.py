# commands imports
from django.core.management.base import BaseCommand

# bs logic import
from core.bslogic.extract import dict_extract
from core.bslogic.evolutions import add_evolutions

# other imports
import requests
import json
import re

# model imports
from pokemon.models import PokemonEvolution
from pokemon.models import Pokemon
from pokemon.models import BaseStats


class Command(BaseCommand):
    help = 'This command allows to fetch information from an API.'

    # allows for command line args
    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        # request for pokemon evolutions
        try:
            request = requests.get(
                f"https://pokeapi.co/api/v2/evolution-chain/{options['id']}"
            )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        json_request = json.dumps(request.json())
        dict_request = json.loads(json_request)
        evolution_chain = dict_request['chain']
        # parsing al the pokemon species using a recurrent function
        species = dict_extract((evolution_chain), 'species')
        evolutions = []

        for specie in species:
            evolution = {}
            # evolution parameters
            pokemon_name = specie['name']
            # remove url and extract id
            pokemon_id = (
                re.findall(
                    r"(\/[0-9]+\/)$",
                    specie['url']
                )
            )[0].replace('/', "")

            try:
                request = requests.get(
                    f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
                )
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

            json_request = json.dumps(request.json())
            dict_request = json.loads(json_request)
            # pokemon general stats
            height = int(dict_request['height'])

            weight = int(dict_request['weight'])
            # pokemon base stats
            dict_base_stats = dict_request['stats']
            basic_stats = {}
            for stat in dict_base_stats:
                stat_name = stat['stat']['name']
                base_stat = stat['base_stat']
                basic_stats[stat_name] = base_stat

            # object creation

            PokemonEvolution.objects.get_or_create(
                id=pokemon_id,
                name=pokemon_name
            )

            BaseStats.objects.get_or_create(
                id=pokemon_id,
                hp=basic_stats['hp'],
                attack=basic_stats['attack'],
                defense=basic_stats['defense'],
                special_attack=basic_stats['special-attack'],
                special_defense=basic_stats['special-defense'],
                speed=basic_stats['speed']
            )

            base_stat_object = BaseStats.objects.get(pk=pokemon_id)
            Pokemon.objects.get_or_create(
                id=pokemon_id,
                name=pokemon_name,
                base_stats=base_stat_object,
                weight=weight,
                height=height
            )
            # create a list of evolutions id's avaliable
            evolution['id'] = pokemon_id
            evolutions.append(evolution)
        # adding evolutions to pokemon models
        add_evolutions(evolutions)
        print(f"!!!{len(evolutions)} pokemon added/updated to pokedex!!!")
