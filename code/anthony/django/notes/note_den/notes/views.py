from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note


def index(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, "notes/index.html", context)


# Request Methods:
# GET
# POST
# PUT
# PATCH
# DELETE
# OPTIONS

def note_submission(request):
    # grab all the form data from request.POST
    form = request.POST
    title = form['title']
    summary = form['summary']
    tag = form['tag']

    # create a new note
    new_note = Note()
    new_note.title = title
    new_note.summary = summary
    new_note.tag = tag

    # .save() will store our new note in our database
    new_note.save()

    return redirect('index')


def delete_note(request, note_id):
    note_to_remove = Note.objects.get(id=note_id)
    note_to_remove.delete()

    return redirect('index')
