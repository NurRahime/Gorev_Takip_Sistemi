from django.urls import path
from . import views

urlpatterns = [
    path("", views.category_list, name="category_list"),
    path("edit/<int:pk>/", views.edit_category, name="edit_category"),
    path("delete/<int:pk>/", views.delete_category, name="delete_category"),
]
