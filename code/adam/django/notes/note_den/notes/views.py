from django.shortcuts import render
from .models import Note

# Create your views here.
def index(request):
   notes = Note.objects.all()
   context = {
      "notes": notes
   }
   return render(request, "notes/index.html", context)

