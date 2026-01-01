from django.urls import path
from . import views

urlpatterns = [
    path('archive/', views.arcihve, name='archive'),
    path('notifications/', views.notifications, name='notifications'),
]