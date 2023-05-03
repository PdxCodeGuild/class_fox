from django.shortcuts import redirect, render
from .models import GroceryItem


def home(request):
    grocery_items = GroceryItem.objects.all()

    purchased_items = grocery_items.filter(purchased=True)
    non_purchased_items = grocery_items.filter(purchased=False)

    context = {
        'purchased_items': purchased_items,
        'non_purchased_items': non_purchased_items
    }

    return render(request, 'grocery_list/home.html', context)


def add_item(request):
    if request.method == "POST":
        form = request.POST
        new_item = GroceryItem()
        new_item.name = form['food_name']
        new_item.quantity = form['quantity']
        new_item.save()

    return redirect('home')


def toggle_purchased(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    if item.purchased == True:
        item.purchased = False
    else:
        item.purchased = True

    item.save()

    return redirect('home')


def delete_item(request, item_id):
    grocery_item_delete = GroceryItem.objects.get(id=item_id)
    grocery_item_delete.delete()

    return redirect('home')
