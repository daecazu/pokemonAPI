from django.test import TestCase
import json

# import the bussiness logic files
from core.bslogic.extract import dict_extract
from core.bslogic.evolutions import add_evolutions

# model imports
from pokemon.models import PokemonEvolution
from pokemon.models import Pokemon
from pokemon.models import BaseStats


def sample_pokemon(
    id=1,
    name="bulbasaur",
    hp=45,
    attack=49,
    defense=49,
    special_attack=65,
    special_defense=65,
    speed=45
):
    PokemonEvolution.objects.create(
        id=id,
        name=name
    )
    stat = BaseStats.objects.create(
        id=id,
        hp=hp,
        attack=attack,
        defense=defense,
        special_attack=special_attack,
        special_defense=special_defense,
        speed=speed
    )
    return Pokemon.objects.create(
        id=id,
        name=name,
        base_stats=stat,
        weight=10,
        height=100
    )


def sample_json():
        with open('core/tests/json_text.txt') as json_file:
            data_json = json.load(json_file)
            return(data_json)


class BussinesLogicTest(TestCase):

    def test_extract_dict(self):
        """Test the function retrieves the species of pokemon"""
        species_list = [
            {
                "name": "venusaur",
                "url": "https://pokeapi.co/api/v2/pokemon-species/3/"
            },
            {
                "name": "ivysaur",
                "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
            },
            {
                "name": "bulbasaur",
                "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
            }
        ]
        evolution_json = sample_json()
        species = dict_extract(evolution_json, 'species')
        self.assertEqual(species, species_list)

    def test_add_evolutions(self):
        id_list = [
            {'id': 1},
            {'id': 2},
            {'id': 3}
        ]
        evo1 = sample_pokemon(id=1, name="bulbasaur")
        evo2 = sample_pokemon(id=2, name="ivysaur")
        evo3 = sample_pokemon(id=3, name="venusaur")
        add_evolutions(id_list)
        # counts
        count1 = evo1.evolutions.count()
        count2 = evo2.evolutions.count()
        count3 = evo3.evolutions.count()

        self.assertFalse(evo1.evolutions.filter(id=1).exists())
        self.assertEqual(count1, 2)

        self.assertFalse(evo2.evolutions.filter(id=2).exists())
        self.assertEqual(count2, 2)

        self.assertFalse(evo3.evolutions.filter(id=3).exists())
        self.assertEqual(count3, 2)
