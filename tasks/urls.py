from django.urls import path
from . import views

urlpatterns = [
    path('task_form/', views.task_form_view, name='task_form'),
    path('task_list/', views.task_list_view, name='task_list'),
]