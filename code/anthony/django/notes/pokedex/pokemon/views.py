from django.shortcuts import render
from .models import Pokemon, Type, Ability


def all_pokemon(request):
    pokemon = Pokemon.objects.all()[:20]

    context = {
        "pokemon": pokemon
    }

    return render(request, "pokemon/pokedex.html", context)


def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)

    context = {
        "pokemon": pokemon
    }

    return render(request, "pokemon/detail.html", context)
