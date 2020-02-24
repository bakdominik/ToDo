from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='userhome'),
    path('tasks', views.tasks, name='tasks'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('mark_as_done', views.mark_as_done, name='mark_as_done'),
    path('show_all_tasks', views.show_all_tasks, name='show_all_tasks'),
]