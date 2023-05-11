from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User
from posts.models import Post


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
       
    else:
        form = UserCreationForm()
        context = {
                'form': form
            }
        return render(request, 'users/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('home')
        
    else:
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
    

def profile(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'users/profile.html', context)
