from django.shortcuts import render, redirect
from .models import Note
from django.http import HttpResponse

def index(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, "notes/index.html", context)
def note_submission(request):
    form = request.POST
    title = form['title']
    summary = form['summary']
    tag = form['tag']

    new_note = Note()
    new_note.title = title
    new_note.summary = summary
    new_note.tag = tag
    new_note.save()


    return redirect('index')

def delete_note(request, note_id):
    note_to_remove = Note.objects.get(id=note_id)
    note_to_remove.delete()

    return redirect('index')

