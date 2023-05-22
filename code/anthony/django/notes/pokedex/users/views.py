from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth


def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            # TODO: Redirect to team page
            return redirect('all_pokemon')

    return render(request, "users/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect('all_pokemon')
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect('all_pokemon')
