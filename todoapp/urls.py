from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='userhome'),
    path('tasks', views.tasks, name='tasks'),
    path('delete_task', views.delete_task, name='delete_task'),
]