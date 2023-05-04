from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def fox(request):
    return render(request, "first_app/fox.html")

def osprey(request):
    return HttpResponse("Hello class osprey!")

def cohort(request, class_name):
    context = {
        "name_of_class": class_name
    }
    return render(request, "first_app/cohort.html", context)