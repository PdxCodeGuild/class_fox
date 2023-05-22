from django.shortcuts import render, redirect
from .models import Team
from django.contrib.auth.decorators import login_required
from pokemon.models import Pokemon


@login_required()
def home(request):
    if request.method == "POST":
        form = request.POST
        Team.objects.create(
            name=form["team-name"],
            description=form["team-description"],
            user=request.user
        )

    teams = Team.objects.filter(user=request.user)
    context = {
        "teams": teams,
    }
    return render(request, "teams/home.html", context)


@login_required()
def add_pokemon(request):
    if request.method == "POST":
        # TODO: Find the "django" way to do this...
        form = dict(request.POST)
        team_id = form['selected-team'][0]
        team = Team.objects.get(id=int(team_id))
        for pokemon_id in form["selected-pokemon"]:
            if len(team.pokemon.all()) == 6:
                break
            team.pokemon.add(int(pokemon_id))
            team.save()

    return redirect('home')


def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)

    context = {
        "team": team
    }

    return render(request, 'teams/team_detail.html', context)
