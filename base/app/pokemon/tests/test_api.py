# Django general imports
from django.urls import reverse
from django.test import TestCase

# Django Rest Framework imports
from rest_framework import status
from rest_framework.test import APIClient

# model imports
from pokemon.models import PokemonEvolution
from pokemon.models import Pokemon
from pokemon.models import BaseStats

# import the bussiness logic files
from core.bslogic.evolutions import add_evolutions

POKEMON_URL = reverse('pokemon:pokemon-list')


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


class PublicReportesApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_pokemon(self):

        sample_pokemon(id=4, name="charmander")
        sample_pokemon(id=5, name="charmeleon")
        sample_pokemon(id=6, name="charizard")

        response = self.client.get(POKEMON_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_pokemon_search(self):

        sample_pokemon(id=4, name="charmander")
        sample_pokemon(id=5, name="charmeleon")
        sample_pokemon(id=6, name="charizard")

        response = self.client.get(
            POKEMON_URL,
            {'search': 'charm'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_charmander_search(self):

        sample_pokemon(id=4, name="charmander")
        sample_pokemon(id=5, name="charmeleon")
        sample_pokemon(id=6, name="charizard")
        id_list = [
            {'id': 4},
            {'id': 5},
            {'id': 6}
        ]
        add_evolutions(id_list)
        response = self.client.get(
            POKEMON_URL,
            {'search': 'charmander'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
