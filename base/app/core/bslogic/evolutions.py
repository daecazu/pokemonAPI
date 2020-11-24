"""adding evolutions to pokemon model"""
# model imports
from pokemon.models import PokemonEvolution
from pokemon.models import Pokemon


def add_evolutions(evolutions):
    """add evolution objects to pokemon objects"""
    for pokemon in evolutions:
        pokemon_id = pokemon['id']
        pokemon_object = Pokemon.objects.get(id=pokemon_id)
        for evolution in evolutions:
            evolution_id = evolution['id']
            if(evolution_id != pokemon_id):
                evolution_object = PokemonEvolution.objects.get(
                    id=evolution_id
                )
                pokemon_object.evolutions.add(evolution_object)
