from django.db import models
from pokemon.models import Pokemon
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=32)
    pokemon = models.ManyToManyField(Pokemon, related_name="teams")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name
