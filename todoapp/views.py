from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todoapp/home.html', context)

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'todoapp/task_form.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'todoapp/task_form.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request, 'todoapp/delete_form.html', context)