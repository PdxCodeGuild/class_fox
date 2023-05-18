from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
