"""Pokemon Serializers"""

# Django REST framework

from rest_framework import serializers

# model imports

from pokemon.models import Pokemon
from pokemon.models import BaseStats


class PokemonEvolutionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    evolution_type = serializers.SerializerMethodField()

    def get_evolution_type(self, obj):
            return "Evolution"


class PokemonBasicStatsSerializer(serializers.Serializer):
    hp = serializers.IntegerField()
    defense = serializers.IntegerField()
    attack = serializers.IntegerField()
    special_attack = serializers.IntegerField()
    special_defense = serializers.IntegerField()
    speed = serializers.IntegerField()

    class Meta:
        model = BaseStats


class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    height = serializers.IntegerField()
    weight = serializers.IntegerField()
    base_stats = PokemonBasicStatsSerializer(read_only=True)
    evolutions = PokemonEvolutionSerializer(
        many=True

        )

    class Meta:
        model = Pokemon
