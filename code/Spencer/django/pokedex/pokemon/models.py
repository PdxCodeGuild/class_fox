from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10, null = True, blank = True)

    def __str__(self):
        return self.name
    
class Ability(models.Model):
    name = models.CharField(max_length=10)
    effect = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=15)
    height = models.FloatField()
    weight = models.FloatField()
    number = models.IntegerField()
    image_url = models.URLField()
    abilities = models.ManyToManyField(Ability, related_name="pokemon")
    types = models.ManyToManyField(Type, related_name="pokemon")

    def __str__(self):
        return self.name

