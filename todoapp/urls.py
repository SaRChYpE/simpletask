from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-view'),
    path('create-task', views.create_task, name='task-create'),
    path('update-task/<str:pk>', views.update_task, name='task-update'),
    path('delete-task/<str:pk>', views.delete_task, name='task-delete')
]