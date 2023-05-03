
# Lab 2: URL Shortener

## Let's create a simple URL shortener app.

In this lab, we will be creating a simple `url_shortener` app using Django. A url shortener is a web service that can take long urls (`https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url&gs_l=psy-ab.3..0i22i30k1.1095.3196.0.3437.19.18.0.0.0.0.137.1480.14j4.18.0....0...1.1.64.psy-ab..1.18.1477.0..0j35i39k1j0i131k1j0i67k1j0i20i264k1j33i22i29i30k1.0.aJvctrIr-Ds`) and create a short url (`goo.gl/pEc4vt`).

For example: [TinyURL](https://tinyurl.com/) is a popular url shortener.

When the short url is accessed, the view will take the specific `code` associated with that url (`pEc4vt`) and look up the url associated with it in the database. If that URL is found, it then redirects to that URL.

| id  | code     | url                                  |
| --- | -------- | ------------------------------------ |
| `1` | `pEc4vt` | `https://www.google.com/search?s...` |
| `2` | `fso3Fs` | `https://www..`                      |

You *could* use the ID in the url, instead of some code, but that then exposes some details about your database to the public.

#### *HINT: Remember the random password generator lab in python? Might be helpful in creating a random code*

Let's get started!

### **Step 1**: Create a new Django project and app

First, create a new Django project called `lab2` and a new app called `url_shortener`.

```bash
$ django-admin startproject lab2
$ cd lab2
$ python manage.py startapp url_shortener
```

Add the `url_shortener` app to the `INSTALLED_APPS` list in `lab2/settings.py`.

```python
INSTALLED_APPS = [
    'url_shortener',
    ...
]
```

### **Step 2**: Create the `Link` model

Create a model called `Link` in `url_shortener/models.py` that has the following fields:

- `url` - a `CharField` that stores the long url
    - Reminder: `CharField` has a required `max_length` parameter
- `code` - a `CharField` that stores the short code
    - Reminder: `CharField` has a required `max_length` parameter
    - Let's set our `max_length` to 6 characters
- `created_at` - a `DateTimeField` that stores the date and time the link was created
    - Reminder `DateTimeField` has an `auto_now_add` parameter that will automatically set the field to the current date and time when the object is first created.

```python
from django.db import models

class Link(models.Model):
    # TODO: add fields here
```

> Challenge: What method can you add to the `Link` model to make it easier to print out the object? For example the admin site displays by default `Link object (1)` for the first `Link` object. How can you change that to display something more meaningful?

### **Step 3**: Add `Link` to the admin site

Register the `Link` model in `url_shortener/admin.py` so that you can add and edit links in the admin site.

```python
from django.contrib import admin

from .models import Link

admin.site.register(Link)
```

Run the migrations to create the `Link` table in the database.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Knowledge Check: What is the difference between `makemigrations` and `migrate`? Leave your response in a file called `knowledge_check.md` in the `lab2` directory.

Create a superuser so that you can log into the admin site.

```bash
$ python manage.py createsuperuser
```

Start the server and log into the admin site at `http://127.0.0.1:8000/admin/`.

```bash
$ python manage.py runserver
```

> Try adding a few links in the admin site. You can use random characters for the code.

### **Step 4**: Display Links on your home page

Create a view called `home` in `url_shortener/views.py` that will display all the links in the database. You can use the `Link.objects.all()` method to get all the links.

```python
from django.shortcuts import render

from .models import Link

def home(request):
  # TODO: get all the links from the database

  # TODO: create a context dictionary to pass to the template

  # TODO: render the template

```

Create a template called `home.html` in `url_shortener/templates/url_shortener/` that will display all the links in the database. You can use the following template as a starting point.

```html
  <h1>Links</h1>
  <table>
    <thead>
      <tr>
        <th>Code</th>
        <th>URL</th>
      </tr>
    </thead>
    <tbody>
      {% for link in links %}
      <tr>
        <td>{{ link.code }}</td>
        <td>{{ link.url }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
```

> Challenge: Can you modify the table in our html file to display the `created_at` field as well?

Add a url pattern in `url_shortener/urls.py` that will map the `home` view to the root url.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Add the `url_shortener` app's urls to the `lab2/urls.py` file.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('url_shortener.urls')),
]
```

### **Step 5**: Create the `add_link` view

Let's add a form to the home page so that we can add new links.

```html
  <h2>Add a Link</h2>
  <form action="{% url 'add_link' %}" method="post">
    {% csrf_token %}
    <label>
      URL
      <input type="text" id="url">
    </label>
    <input type="submit" value="Add">
  </form>
```

> Challenge: What required property is missing from the `input` tag with the id of `url`?

Create a view called `add_link` in `url_shortener/views.py` that will handle the form submission. You can use the `request.POST` dictionary to get the data from the form.

```python
def add_link(request):
  form = request.POST
  new_link = Link()
  new_link.url = form['url']

  # TODO: generate a random 6 character code and assign it to new_link.code

  new_link.save()

  return redirect('home')
```

> Challenge: Generate a random 6 character code for the `code` field. Think back to the random password generator lab in python.

Add a url pattern in `url_shortener/urls.py` that will map the `add_link` view to the `/add_link` url.

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('add_link', views.add_link, name='add_link'),
]
```

> Test out your form by adding a few links. You should see the links appear on the home page.

### **Step 6**: Create the `redirect_link` view

Now that we have a way to add links, let's create a way to redirect users to the long url when they visit the short url.

Create a view called `redirect_link` in `url_shortener/views.py` that will redirect the user to the long url.

```python
def redirect_link(request, code):
  link = Link.objects.get(code=code)
  return redirect(link.url)
```

Add a url pattern in `url_shortener/urls.py` that will map the `redirect_link` view to the `/r/<code>` url.

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('add_link', views.add_link, name='add_link'),
    path('r/<code>', views.redirect_link, name='redirect_link'),
]
```

> Test out your redirect by visiting `http://127.0.0.1:8000/r/<code>` in your browser. You should be redirected to the long url.

### **Step 7**: Add a counter to keep track of the number of times a link is visited

1. Add a `counter` field to the `Link` model. The `counter` field should be an `IntegerField` with a default value of `0`.
2. Update the table in `home.html` to display the `counter` field.
3. Update the `redirect_link` view to increment the `counter` field by 1 each time the link is visited.
   1. We have the `link` object, so we can just increment the `counter` field and save the object.

> (Optional) Challenge: Update the `code` field in your table to be a link to the short url. You can use the `url` template tag to generate the url.
> (Optional) Challenge: Add a `last_visited` field to the `Link` model. The `last_visited` field should be a `DateTimeField` with `auto_now=True`, this was each time a count is incremented, the `last_visited` field will be updated with the current time. Update the table in `home.html` to display the `last_visited` field in your table.
