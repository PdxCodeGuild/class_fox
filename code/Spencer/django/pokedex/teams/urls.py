from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("team/<int:team_id>/", views.team_detail, name="team_detail"),
    
]
