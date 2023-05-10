from django.shortcuts import render, redirect
from .models import GroceryItem
# Create your views here.

def home(request):
    # GroceryItem.objects.all() will return all of the GroceryItem objects in the database
    grocery_items = GroceryItem.objects.all()
    purchased_items = grocery_items.filter(purchased=True)
    # Filter the grocery items to get the non purchased items
    non_purchased_items = grocery_items.filter(purchased=False)
    context = {
        'purchased_items': purchased_items,
        'non_purchased_items': non_purchased_items,
        'grocery_items': grocery_items
        }

    return render(request, 'grocery_list/home.html', context)

def add_item(request):
    if request.method == 'POST':
        form = request.POST
        # Create a new GroceryItem object
        new_item = GroceryItem(default=1)
        # Set the name field to the name from the form
        new_item.name = form['name']
        # Save the new GroceryItem object to the database
        new_item.save()
        # Redirect to the home page
        return redirect('home')

def mark_purchased(request, item_id):
    # Get the GroceryItem object with the id item_id
    item = GroceryItem.objects.get(id=item_id)
    # Set the purchased field to True
    if item.purchased == True:
        item.purchased = False
    else: 
        item.purchased = True
    # Save the GroceryItem object to the database
    item.save()
    # Redirect to the home page
    return redirect('home')

def delete_item(request, item_id):
    item_to_remove = GroceryItem.objects.get(id=item_id)
    item_to_remove.delete()
    return redirect('home')