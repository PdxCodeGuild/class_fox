from django.shortcuts import render, redirect
from .models import Todo, Priority
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    todos = Todo.objects.filter(
        is_completed=False, user=request.user).order_by('-priority__value')
    priorities = Priority.objects.all()

    context = {
        "todos": todos,
        "priorities": priorities
    }
    return render(request, 'todos/home.html', context)


def create_todo(request):
    if request.user.is_authenticated:
        form = request.POST
        todo_text = form['text']
        priority_id = form['priority']

        priority = Priority.objects.get(id=priority_id)

        new_todo = Todo()
        new_todo.text = todo_text
        new_todo.priority = priority
        new_todo.user = request.user  # request.user is the current logged in user
        new_todo.save()

        return redirect('home')
    else:
        return redirect('login')
