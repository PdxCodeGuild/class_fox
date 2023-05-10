from django.shortcuts import render, redirect
from .models import Link
import string
import random


def home(request):

    all_links = Link.objects.all().order_by('-counter')

    context = {
        'links': all_links
    }

    return render(request, 'url_shortener/home.html', context)

def add_link(request):

    if request.method == "POST":
        form = request.POST

        new_link = Link()
        new_link.url = form['url']

        # code = ""
        # for x in range(6):
        #     code += random.choice(string.ascii_letters + string.digits)

        code = "".join(random.choices(string.ascii_letters + string.digits, k=6))

        new_link.code = code

        new_link.save()

        return redirect('home')
    else:
        return redirect('home')


def redirect_link(request, url_code):
    link = Link.objects.get(code=url_code)
    link.counter = link.counter + 1
    link.save()
    return redirect(link.url)


def delete_link(request, link_id):
    Link.objects.get(id=link_id).delete()
    return redirect('home')