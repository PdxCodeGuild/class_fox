from django.shortcuts import render, redirect
from .models import Link

import random
import string

# Create your views here.

def home(request):
    # TODO: get all the links from the database
    all_links = Link.objects.all().order_by('-clicks')
     # TODO: create a context dictionary to pass to the template
    context = {
        "all_links": all_links
    }

    # TODO: render the template
    return render(request, 'url_shortener/home.html', context)

def add_link(request):
    form = request.POST
    new_link = Link()
    new_link.url = form['url']

  # TODO: generate a random 6 character code and assign it to new_link.code
    letters = string.ascii_letters
    digits = string.digits
    character_code = letters + digits
   
    shortened_url = []
    for x in range (6):
        shortened_url.append(random.choice(character_code))
    
    new_link.code = ''.join(shortened_url)


    new_link.save()

    return redirect('home')


def redirect_link(request, code):
  link = Link.objects.get(code=code)
  link.clicks += 1
  link.save()
  return redirect(link.url)

def delete_link(request, link_id):
    url_link_delete = Link.objects.get(id=link_id)
    url_link_delete.delete()

    return redirect('home')
