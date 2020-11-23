""" Pokemon models """


# Django
from django.db import models


class PokemonEvolution(models.Model):
    id = models.IntegerField(
        primary_key=True,
        blank=False,
        null=False
    )
    name = models.CharField(
        max_length=20,
        blank=False,
        null=False
    )

    def __str__(self):
        return f"name:{self.name}"


class BaseStats(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    hp = models.IntegerField()
    defense = models.IntegerField()
    attack = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return f"id:{self.id}"


class Pokemon(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        max_length=20,
        blank=False,
        null=False
    )
    base_stats = models.OneToOneField(
        BaseStats,
        on_delete=models.CASCADE,
    )
    weight = models.IntegerField()
    height = models.IntegerField()
    evolutions = models.ManyToManyField('PokemonEvolution')

    def __str__(self):
        return f"id:{self.id}"
