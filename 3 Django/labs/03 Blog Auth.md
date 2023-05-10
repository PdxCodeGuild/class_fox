# Lab 3 Blog Auth Implementation

## Implementing Auth in a premade Django Blog

In this lab, you will be implementing authentication in a premade Django blog. The blog is already made, but it is missing the ability for users to sign up, log in, and log out. You will be adding these features to the blog.

---

Let's get started!

### **Step 1***: Copy the starter code

Copy the starter code from the [starter code folder](./blog_auth/) into your code folder.

---

### **Step 2**: Getting setup

Make sure you are in the directory of your `blog_auth` project.

Makemigrations and migrate to apply the models to your own database.

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the `loaddb` command to load the database with some data. This will add users and posts to your database.

```bash
python manage.py loaddb
```

Run the server and make sure everything is working.

```bash
python manage.py runserver
```

Check your admin site to make sure the users and posts were added to your database.

---

### **Step 3**: Adding the signup page

In `users/views.py`, add the following code to the `signup` function:

```python
if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        auth.login(request, user)
        return redirect('home')
else:
    form = UserCreationForm()
```

Be sure to import the `UserCreationForm` from `django.contrib.auth.forms` and the `auth` function from `django.contrib`.

Add your form to the context dictionary:

```python
context = {
    'form': form
}
```

and pass this to the `render` function.

In `users/templates/users/signup.html`, add the following code:

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
```

> Try it out! Can you create a new user? Try going to 127.0.0.1/users/signup and creating a new user. Check your admin site to make sure the user was added to your database.

---

### **Step 4**: Adding the login page

In `users/views.py`, add the following code to the `login` function:

```python
if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        auth.login(request, form.get_user())
        return redirect('home')
else:
    form = AuthenticationForm()
```

Be sure to import the `AuthenticationForm` from `django.contrib.auth.forms` and the `auth` function from `django.contrib`.

Add your form to the context dictionary:

```python
context = {
    'form': form
}
```

and pass this to the `render` function.

In `users/templates/users/login.html`, add the following code:

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
</form>
```

> Try it out! Can you log in? Try going to 127.0.0.1/users/login and logging in with one of the users you created. Check your admin site to make sure the user was added to your database.


---

### **Step 5**: Adding a logout feature

In `users/views.py`, add the following code to the `logout` function:

```python
auth.logout(request)
return redirect('home')
```

Be sure to import the `auth` function from `django.contrib`.

> Try it out! Can you log out? Try clicking on the logout button at the top of the page. You should notice that it now shows a login button. Try logging in again. You should notice that it now shows a logout button.

---

### **Step 6**: Adding a user profile page

In `users/views.py`, create a new function called `profile`:

```python
def profile(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(author=user).order_by('-date')
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'users/profile.html', context)
```

In `users/urls.py`, add the following code:

```python
path('<int:pk>/', views.profile, name='profile'),
```

In `users/templates/users/profile.html`, add the following code:

```html
<h1>{{ user.username }}</h1>
{% for post in posts %}
<article>
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
</article>
{% endfor %}
```

> Challenge: Can you add a link to the user's profile page on the home page? On each post, try adding a link to the user's profile page. You will need to pass the user's id to the profile page. You can do this by adding `post.author.id` in the href. For example, `<a href="{% url 'profile' post.author.id %}">{{ post.author }}</a>`

> Try it out! Can you view a user's profile? Try clicking on the link to the user's profile page. You should see a list of all the posts that user has made.

---

### **Step 7**: Adding auth protection to `posts/views.py`

In `posts/views.py`, I have left comments asking you to add auth protection to the `post_create`, `post_edit`, and `post_delete` functions.

You can check to see if a user is logged in by using the `request.user.is_authenticated` function. If the user is not logged in, you can redirect them to the login page.