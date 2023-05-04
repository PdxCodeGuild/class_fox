from django.shortcuts import render, redirect
from .models  import Groceryitem

# Create your views here.
def home(request):
    grocery_items = Groceryitem.objects.all()

    purchased_items = grocery_items.filter(purchased=True)

    non_purchased_items = grocery_items.filter(purchased=False)

    context = {
        'purchased_items': purchased_items,
        'non_purchased_items': non_purchased_items
    }

    return render(request, 'grocery_list/home.html', context)

def add_item(request):
    if request.method == 'POST':
        form = request.POST
        # Create a new GroceryItem object
        new_item = Groceryitem()
        # Set the name field to the name from the form
        new_item.name = form['name']
       
        # Set quantity field of new grocery item
        new_item.quantity = form['quantity']
       
       # Save the new GroceryItem object to the database
        new_item.save()
        # Redirect to the home page
        return redirect('home')
    
def mark_purchased(request, item_id):
    # Get the GroceryItem object with the id item_id
    item = Groceryitem.objects.get(id=item_id)
    
    if item.purchased == True:
        item.purchased = False
    else: item.purchased = True
    # Save the GroceryItem object to the database
    item.save()
    # Redirect to the home page
    return redirect('home')

def delete_item(request, item_id):
    grocery_item_delete = Groceryitem.objects.get(id=item_id)
    grocery_item_delete.delete()
    return redirect('home')