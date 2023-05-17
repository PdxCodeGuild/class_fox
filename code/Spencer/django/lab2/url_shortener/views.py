from django.shortcuts import render
from .models import Link
import random
import string
from django.shortcuts import redirect



def home(request):
    links = Link.objects.all()
    context = {
            'links' : links

    }
    return render(request, 'url_shortener/home.html', context)

def add_link(request):
  form = request.POST
  new_link = Link()
  new_link.url = form['url']
  code = ""
  for x in range(6):
    code = code + random.choice(string.ascii_letters + string.digits)

  new_link.code = code
  new_link.save()

  return redirect('home')

def redirect_link(request, code):
  link = Link.objects.get(code=code)
  counter = counter + 1
  return redirect(link.url)

def delete_item(request, link):
    link_to_remove = Link.objects.get(id=link)
    link_to_remove.delete()
    return redirect('home')