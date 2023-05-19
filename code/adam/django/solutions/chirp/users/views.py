from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib import auth

# function allows user to signup
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()

        return render(request, 'users/signup.html', {'form': form})
    

# function that allows user to login
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('home')
    
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    

# function that lets user logout
def logout(request):
    auth.logout(request)
    return redirect('home')

# function that lets user look at other profiles
def profile(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'users/profile.html', context)