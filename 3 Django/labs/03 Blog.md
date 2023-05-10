# Lab 2: Simple Blog App

## Let's create a simple blog app.

In this lab, we will be creating a simple `blog` app using Django. The app will have the following models: `User` and `BlogPost`. We will also include user authentication, a signup/login page, and allow users to create blog posts only if they are logged in. Users can view all blogs on the home page. Clicking on a username will show that user's profile where only posts from that user are visible.

---

Let's walk through each step together.

### **Step 1**: Create a new Django project and app

First, let's create a new Django project called `lab3`.

```bash
$ django-admin startproject lab3
```

Next, let's create a new Django app called `blog`.

```bash
$ cd lab03
$ python manage.py startapp blog
```

Add the new app to the `INSTALLED_APPS` list in `lab3/settings.py`.

```python
INSTALLED_APPS = [
    'blog',
    ...
]
```

---

### **Step 2**: Create the `User` and `BlogPost` models

In `blog/models.py`, create new models called `User` and `BlogPost` with the following fields:

For `User` model, we will use Django's built-in `User` model from `django.contrib.auth.models`.

For `BlogPost` model:

- `author` (models.ForeignKey)
    - Hint: `User` as the model and `on_delete=models.CASCADE`
- `title` (models.CharField)
    - Hint: `max_length=100` 
- `image` (models.URLField)
    - We will set the properties of this field to `blank=True` and `null=True` so that it is not required.
- `content` (models.TextField)
    - models.TextField is similar to models.CharField, but it is used for large amounts of text. It does not have a max_length limit.
- `is_published` (models.BooleanField)
    - Hint: `default=False`
- `created_at` (models.DateTimeField)
    - Hint: `auto_now_add=True` will automatically set the field to the current date and time when the object is first created.
- `updated_at` (models.DateTimeField)
    - Hint: `auto_now=True` will automatically update the field to the current date and time whenever the object is saved.

```python
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

---

### **Step 3**: Add `BlogPost` to the admin site

In `blog/admin.py`, register the `BlogPost` model with the admin site.

```python
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
```

---

### **Step 4**: Migration

Run the migration to create the `BlogPost` table in the database.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

---

### **Step 5**: Create a superuser

Create a superuser so that we can log into the admin site.

```bash
$ python manage.py createsuperuser
```

---

### **Step 6**: Run the server

Run the server and check out the admin site at http://127.0.0.1:8000/admin/.

```bash
$ python manage.py runserver
```

Using the admin site, create a few `User` and `BlogPost` objects.

---

### **Step 7**: Display the blog posts on the home page

In `blog/views.py`, create a new view called `home` that will display the blog posts on the home page.

```python
from django.shortcuts import render
from .models import BlogPost

def home(request):
    # BlogPost.objects.all() will return all of the BlogPost objects in the database
    blog_posts = BlogPost.objects.all()

    context = {'blog_posts': blog_posts}

    return render(request, 'blog/home.html', context)
```

In `blog/urls.py`, create a new path for the home page.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

In `lab02/urls.py`, include the `blog` urls.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

In `blog/templates/blog/home.html`, display the blog posts.

```html
<h1>Posts</h1>
{% for post in blog_posts %}
<div>
    <h2>{{ post.title }}</h2>
    <p>By: {{ post.author }}</p>
    {% if post.image %}
    <img src="{{ post.image }}" alt="post.title">
    {% endif %}
    <p>{{ post.created_at }}</p>
</div>
{% endfor %}
```

---

### **Step 8**: User authentication and signup/login pages

Let's create an app called `auth` for user authentication.

```bash
$ python manage.py startapp auth
```

Add the new app to the `INSTALLED_APPS` list in `lab3/settings.py`.

```python
INSTALLED_APPS = [
    'blog',
    'auth',
    ...
]
```

In `auth/views.py`, create new views for user login and signup.

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
```

In `auth/urls.py`, create new paths for the login, logout, and signup pages.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

In `lab03/urls.py`, include the `auth` urls.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('auth/', include('auth.urls')),
]
```

In `auth/templates/auth/signup.html`, create a signup form.

```html
<h1>Signup</h1>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Signup</button>
</form>

<p>Already have an account? <a href="{% url 'login' %}">Login</a></p>
```

In `auth/templates/auth/login.html`, create a login form.

```html
<h1>Login</h1>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>

<p>Don't have an account? <a href="{% url 'signup' %}">Signup</a></p>
```

In `blog/templates/blog/home.html`, add a link to the login page.

```html
{% if user.is_authenticated %}
<p>Logged in as {{ user.username }}</p>
{% else %}
<p><a href="{% url 'login' %}">Login</a></p>
{% endif %}
```

---

### **Step 9**: Create blog posts only if logged in

In `blog/views.py`, create a new view called `create_post` that allows users to create blog posts only if they are logged in.

```python
from .models import BlogPost
from .forms import BlogPostForm
from django.shortcuts import render, redirect

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            new_post = BlogPost(author=request.user, title=title, content=content)
            new_post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})
```

In `blog/forms.py`, create a new form called `BlogPostForm`.

```python
from django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
```

In `blog/urls.py`, create a new path for the `create_post` view.

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_post/', views.create_post, name='create_post'),
]
```

In `blog/templates/blog/create_post.html`, create a form to create a new blog post.

```html
{% extends 'blog/base.html' %}

{% block content %}
  <h2>Create a new post</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

In `blog/templates/blog/home.html`, add a link to the `create_post` view.

```html
{% if user.is_authenticated %}
  <a href="{% url 'create_post' %}">Create a new post</a>
{% endif %}
```

---

### **Step 10**: User profiles with their blog posts

In `blog/views.py`, create a new view called `user_profile` that displays a user's profile with their blog posts.

```python
def user_profile(request, username):
    user = User.objects.get(username=username)
    user_posts = BlogPost.objects.filter(author=user)
    context = {'user': user, 'posts': user_posts}
    return render(request, 'blog/user_profile.html', context)
```

In `blog/urls.py`, create a new path for the `user_profile` view.

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
]
```

In `blog/templates/blog/user_profile.html`, create a template to display the user's profile with their blog posts.

```html
{% extends 'blog/base.html' %}

{% block content %}
  <h1>{{ user.username }}'s Profile</h1>
  <h2>Blog Posts</h2>
  {% for post in posts %}
    <div>
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <p>Created at: {{ post.created_at }}</p>
    </div>
  {% endfor %}
{% endblock %}
```

In `blog/templates/blog/home.html`, add a link to the `user_profile` view for each blog post author.

```html
{% for post in blog_posts %}
    <div>
        <h2>{{ post.title }}</h2>
        <p>Author: <a href="{% url 'user_profile' post.author.username %}">{{ post.author }}</a></p>
        <p>{{ post.content }}</p>
        <p>Created at: {{ post.created_at }}</p>
    </div>
{% endfor %}
```

---

### **Step 11**: Style your app

Add some CSS to make your app look nice. Since we have not yet covered static files, this can either be done in the `<style></style>` tags in `blog/templates/blog/base.html` or by using a CSS framework. 

For example, you can include Bootstrap CSS in the `<head>` section of `blog/templates/blog/base.html`:

```html
<head>
  <title>Blog</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
```

Then, update your templates to use Bootstrap classes for styling. This is just an example of how to style the app; you can use any CSS framework or write your own custom styles.

---

Now you have a simple blog app with user authentication, a signup/login page, and the ability for users to create blog posts only if they are logged in. Users can view all blogs on the home page, and clicking on a username shows that user's profile where only posts from that user are visible.