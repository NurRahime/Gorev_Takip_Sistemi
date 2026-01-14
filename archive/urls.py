from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.archive_view, name='archive_list'),
    path('notifications/', views.notifications_view, name='notifications_list'),
    path('mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
]