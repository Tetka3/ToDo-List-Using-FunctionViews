from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.order_by('id')
    form = TodoForm()
    return render(request, 'index.html', {'todos':todos, 'form':form})


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(task=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')