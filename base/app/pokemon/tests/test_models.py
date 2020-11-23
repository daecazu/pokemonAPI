from django.test import TestCase
from pokemon.models import PokemonEvolution, Pokemon, BaseStats


def sample_pokemon_evolution(id=1, name="bulbasaur"):
    return PokemonEvolution.objects.create(
        id=id,
        name=name
    )


def sample_base_pokemon_stats(
    id=1,
    hp=45,
    attack=49,
    defense=49,
    special_attack=65,
    special_defense=65,
    speed=45
):
    return BaseStats.objects.create(
        id=id,
        hp=hp,
        attack=attack,
        defense=defense,
        special_attack=special_attack,
        special_defense=special_defense,
        speed=speed
    )


class ModelTests(TestCase):

    def test_model_str(self):
        """ test pokemon evolution model"""
        pokemon_evolution = sample_pokemon_evolution()

        self.assertEqual(
            str(pokemon_evolution),
            f'name:{pokemon_evolution.name}'
        )

    def test_basic_stats_str(self):
        """ test basic stats model"""
        pokemon_stats = sample_base_pokemon_stats()
        self.assertEqual(
            str(pokemon_stats),
            f'id:{pokemon_stats.id}'
        )

    def test_pokemon_str(self):
        """ test pokemon model"""

        pokemon_evolution = sample_pokemon_evolution(id=2, name="ivysaur")
        pokemon_evolution2 = sample_pokemon_evolution(id=3, name="venusaur")
        pokemon_stats = sample_base_pokemon_stats()
        pokemon = Pokemon.objects.create(
            id=1,
            name="bulbasaur",
            base_stats=pokemon_stats,
            weight=1,
            height=2
        )
        pokemon.evolutions.add(pokemon_evolution, pokemon_evolution2)
        self.assertEqual(
            str(pokemon),
            f'id:{pokemon.id}'
        )
