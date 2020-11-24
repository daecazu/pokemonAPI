"""Pokemon views"""

# Django REST Framework
from rest_framework import viewsets

# from rest_framework import generics
from rest_framework import mixins
from rest_framework import filters

# model imports
from pokemon.models import Pokemon

# import
from pokemon.serializers import PokemonSerializer


class PokemonViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
