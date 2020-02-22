from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views.generic.list import ListView
from datetime import date
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated == True:
        return redirect('tasks')
    else:
        return render(request, 'todoapp/home.html')

@login_required()
def tasks(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['date']:
            task = Task()
            task.title = request.POST['title']
            task.date = request.POST['date']
            task.user = request.user
            task.save()
            return redirect('tasks')
        else:
            return render(request, 'todoapp/tasks.html', {'error':'All fields are required'})
    else:
        tasks = Task.objects.filter(user=request.user,date=date.today())
        return render(request, 'todoapp/tasks.html', {'tasks':tasks})

@login_required()
def delete_task(request):
    if request.method == 'POST':
        task = Task.objects.get(pk=request.POST['id'])
        task.delete()
        return redirect('tasks')



        