from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('task_create/', views.task_create_view, name='task_create'),
    path('task_update/<int:id>/', views.task_update_view, name='task_update'),
    path('task_delete/<int:id>/', views.task_delete_view, name='task_delete'),
]