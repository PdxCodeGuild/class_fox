# Lab 1: Grocery List

## Let's create a simple grocery list app. 

In this lab, we will be creating a simple `grocery_list` app using Django. The app will have a single model called `GroceryItem` with the following fields: name, quantity, created_at, purchased.

---

Let's walk through each step together.

### **Step 1**: Create a new Django project and app

First, let's create a new Django project called `lab01`.
    
```bash
$ django-admin startproject lab01
```

Next, let's create a new Django app called `grocery_list`.

```bash
$ cd lab01
$ python manage.py startapp grocery_list
```

Add the new app to the `INSTALLED_APPS` list in `lab01/settings.py`.

```python
INSTALLED_APPS = [
    'grocery_list.apps.GroceryListConfig',
    ...
]
```

---

### **Step 2**: Create the `GroceryItem` model

In `grocery_list/models.py`, create a new model called `GroceryItem` with the following fields:

- `name` (models.CharField)
- `quantity` (models.IntegerField)
- `created_at` (models.DateTimeField)
    - Hint: `auto_now_add=True` will automatically set the field to the current date and time when the object is first created.
- `purchased` (models.BooleanField)
    - Hint: `default=False` will set the default value of the field to `False` if no value is provided.

```python
from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    purchased = models.BooleanField(default=False)
```

> Challenge: Is it possible to set a default quantity of 1 for the `quantity` field?

---

### **Step 3**: Add `GroceryItem` to the admin site

In `grocery_list/admin.py`, register the `GroceryItem` model with the admin site.

```python
from django.contrib import admin
from .models import GroceryItem

admin.site.register(GroceryItem)
```

---

### **Step 4**: Migration

Run the migration to create the `GroceryItem` table in the database.

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

Using the admin site, create a few `GroceryItem` objects.

> Challenge: Notice that in the admin site, grocery items are displayed as `GroceryItem object (1)`. How can we change this to display the name of the grocery item instead?

---

### **Step 7**: Display the grocery list on the home page

In `grocery_list/views.py`, create a new view called `home` that will display the grocery list on the home page.

```python
from django.shortcuts import render
from .models import GroceryItem

def home(request):
    # GroceryItem.objects.all() will return all of the GroceryItem objects in the database
    grocery_items = GroceryItem.objects.all()

    context = {'grocery_items': grocery_items}

    return render(request, 'grocery_list/home.html', context)
```

In `grocery_list/urls.py`, create a new path for the home page.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

In `lab01/urls.py`, include the `grocery_list` urls.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grocery_list.urls')),
]
```

In `grocery_list/templates/grocery_list/home.html`, display the grocery list.

```html
    <h1>Grocery List</h1>
    <ul>
        {% for item in grocery_items %}
            <li>{{ item.name }} - {{ item.quantity }}</li>
        {% endfor %}
    </ul>
```

---

### **Step 8**: Add a new item to the grocery list

In `grocery_list/templates/grocery_list/home.html` create a form to add a new item to the grocery list.

```html
    <form action="" method="POST">
        {% csrf_token %}
        <label>Name:
            <input type="text" name="name">
        </label>
        <label>Quantity:
            <input type="number" name="quantity">
        </label>
        <input type="submit" value="Add">
    </form>
```

> Knowledge check: What is the purpose of the `{% csrf_token %}`? Leave a comment in your form to explain.

In `grocery_list/views.py`, add a new view called `add_item` that will handle the form submission.

```python
from django.shortcuts import render, redirect
from .models import GroceryItem

def add_item(request):
    if request.method == 'POST':
        form = request.POST
        # Create a new GroceryItem object
        new_item = GroceryItem()
        # Set the name field to the name from the form
        new_item.name = form['name']
        # Save the new GroceryItem object to the database
        new_item.save()
        # Redirect to the home page
        return redirect('home')
```

> Challenge: How can we set the `quantity` field of the new `GroceryItem` object?

In `grocery_list/urls.py`, create a new path for the `add_item` view.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
]
```

In `grocery_list/templates/grocery_list/home.html`, add the `action` attribute to the form.

```html
    <form action="{% url 'add_item' %}" method="POST">
```

> Test it out! Try adding a new item to the grocery list using the form.

---

### **Step 9**: Show purchased items and non purchased items in separate lists

In `grocery_list/views.py`, update the `home` view to display purchased items and non purchased items in separate lists.

```python
from django.shortcuts import render
from .models import GroceryItem

def home(request):
    # GroceryItem.objects.all() will return all of the GroceryItem objects in the database
    grocery_items = GroceryItem.objects.all()
    # Filter the grocery items to get the purchased items
    purchased_items = grocery_items.filter(purchased=True)
    # Filter the grocery items to get the non purchased items
    non_purchased_items = grocery_items.filter(purchased=False)

    context = {
        'purchased_items': purchased_items,
        'non_purchased_items': non_purchased_items
    }

    return render(request, 'grocery_list/home.html', context)
```

Update `grocery_list/templates/grocery_list/home.html` to display the purchased items and non purchased items in separate lists.

```html
    <h1>Grocery List</h1>
    <h2>Things to buy</h2>
    <ul>
        {% for item in non_purchased_items %}
            <li>{{ item.name }} - {{ item.quantity }}</li>
        {% endfor %}
    </ul>
    <h2>Purchased Items</h2>
    <ul>
        {% for item in purchased_items %}
            <li>{{ item.name }} - {{ item.quantity }}</li>
        {% endfor %}
    </ul>
```

---

### **Step 10**: Add a button to mark an item as purchased

In `grocery_list/templates/grocery_list/home.html`, add an anchor tag to mark an item as purchased.

```html
    <ul>
        {% for item in non_purchased_items %}
            <li>{{ item.name }} - {{ item.quantity }} <a href="fill this in later">Mark as purchased</a></li>
        {% endfor %}
    </ul>
```

In `grocery_list/views.py`, add a new view called `mark_purchased` that will handle the form submission.

```python
def mark_purchased(request, item_id):
    # Get the GroceryItem object with the id item_id
    item = GroceryItem.objects.get(id=item_id)
    # Set the purchased field to True
    item.purchased = True
    # Save the GroceryItem object to the database
    item.save()
    # Redirect to the home page
    return redirect('home')
```

In `grocery_list/urls.py`, create a new path for the `mark_purchased` view.

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('mark_purchased/<int:item_id>/', views.mark_purchased, name='mark_purchased'),
]
```

In `grocery_list/templates/grocery_list/home.html`, add the `href` attribute to the anchor tag.

```html
    <ul>
        {% for item in non_purchased_items %}
            <li>{{ item.name }} - {{ item.quantity }} <a href="{% url 'mark_purchased' item.id %}">Mark as purchased</a></li>
        {% endfor %}
    </ul>
```

> Test it out! Try marking an item as purchased.

> Challenge: Can we modify the `mark_purchased` view to toggle the `purchased` field instead of setting it to `True`? Hint: Use an if statement.

---

### **Step 11**: Add a button to mark an item as not purchased

In `grocery_list/templates/grocery_list/home.html`, add an anchor tag to mark an item as not purchased.

```html
    <h2>Purchased Items</h2>
    <ul>
        {% for item in purchased_items %}
            <li>{{ item.name }} - {{ item.quantity }} <a href="{% url 'mark_purchased' item.id %}">Mark as not purchased</a></li>
        {% endfor %}
    </ul>
```

---

### **Step 12**: Add a button to delete an item

Using the previous steps for reference, add a button to delete an item: 

- Add an anchor tag to delete an item. This should work on purchased and non purchased items.

- Create a view called `delete_item` that will handle item deletion.

- Create a path for the `delete_item` view.

- Be sure to update your hrefs to use the correct view.

> Test it out! Try deleting an item.

---

### **Step 13**: Style your app

Add some CSS to make your app look nice. Since we have not yet covered static files, this can either be done in the `<style></style>` tags in `grocery_list/templates/grocery_list/home.html` or by using a css framework.