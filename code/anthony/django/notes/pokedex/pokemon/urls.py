from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.all_pokemon, name="all_pokemon"),
    path("<int:pokemon_id>/", views.pokemon_detail, name="pokemon_detail")
]


# 127.0.0.1/pokemon/all/
