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
            if request.POST['all']:
                return redirect('show_all_tasks')
            return redirect('tasks')
        else:
            tasks = Task.objects.filter(user=request.user,date=date.today())
            return render(request, 'todoapp/tasks.html', {'show':'Today','error':'All fields are required','tasks':tasks,'date':date.today().isoformat()})
    else:
        tasks = Task.objects.filter(user=request.user,date=date.today())
        return render(request, 'todoapp/tasks.html', {'show':'Today','tasks':tasks,'date':date.today().isoformat()})

@login_required()
def delete_task(request):
    if request.method == 'POST':
        task = Task.objects.get(pk=request.POST['id'])
        task.delete()
        if request.POST['all']:
            return redirect('show_all_tasks')
        return redirect('tasks')

@login_required()
def mark_as_done(request):
    if request.method == 'POST':
        task = Task.objects.get(pk=request.POST['id_checked'])
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True
        task.save()
    return redirect('tasks')

@login_required()
def show_all_tasks(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['date']:
            task = Task()
            task.title = request.POST['title']
            task.date = request.POST['date']
            task.user = request.user
            task.save()
            return redirect('tasks')
        else:
            tasks = Task.objects.filter(user=request.user,date=date.today())
            return render(request, 'todoapp/tasks.html', {'show':'All tasks','error':'All fields are required','tasks':tasks,'date':date.today().isoformat()})
    else:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'todoapp/tasks.html', {'show':'All tasks','all':True,'tasks':tasks,'date':date.today().isoformat()})