from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_view, name='task_list'),# liste çağırır
    path('task_create/', views.task_create_view, name='task_create'), #fromu çağırır
    path('task_update/<int:id>/', views.task_update_view, name='task_update'), # güncelleme sayfasını çağırır
]