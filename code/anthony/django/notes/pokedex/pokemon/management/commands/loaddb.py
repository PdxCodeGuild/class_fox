from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type, Ability
import requests
from time import sleep


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Clear out old data from db
        Pokemon.objects.all().delete()
        Type.objects.all().delete()
        Ability.objects.all().delete()

        # Get all pokemon from pokemonAPI
        limit = 1281
        all_pokemon_url = f"https://pokeapi.co/api/v2/pokemon/?limit={limit}"
        list_of_pokemon_urls = requests.get(all_pokemon_url).json()

        # For each pokemon
        counter = 0
        for poke_url in list_of_pokemon_urls["results"]:
            counter += 1
            print(f"currently on pokemon #{counter} of {limit}")
            sleep(.5)
            single_pokemon_url = poke_url["url"]
            # get data
            pokemon_data = requests.get(single_pokemon_url).json()

            new_pokemon = Pokemon()
            new_pokemon.name = pokemon_data["name"]
            new_pokemon.height = pokemon_data["height"]
            new_pokemon.weight = pokemon_data["weight"]
            new_pokemon.number = pokemon_data["id"]
            new_pokemon.image_url = pokemon_data["sprites"]["front_default"]

            new_pokemon.save()

            # get abilities
            for ability in pokemon_data["abilities"]:
                # If there is already an ability with this name in our db, continue
                if Ability.objects.filter(name=ability["ability"]["name"]).exists():
                    new_ability = Ability.objects.get(
                        name=ability["ability"]["name"])
                else:
                    ability_data = requests.get(
                        ability["ability"]["url"]).json()
                    new_ability = Ability()
                    new_ability.name = ability_data["name"]

                    for effect in ability_data["effect_entries"]:
                        if effect["language"]["name"] == "en":
                            new_ability.effect = effect["short_effect"]

                    new_ability.save()

                new_pokemon.abilities.add(new_ability)
                new_pokemon.save()

            # get types
            for type in pokemon_data["types"]:
                type_obj = Type.objects.filter(name=type["type"]["name"])
                if not type_obj.exists():
                    type_obj = Type()
                    type_obj.name = type["type"]["name"]
                    type_obj.save()

                    new_pokemon.types.add(type_obj)
                else:
                    new_pokemon.types.add(type_obj[0])
                new_pokemon.save()
