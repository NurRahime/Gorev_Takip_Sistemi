from django.urls import path
from . import views

urlpatterns = [
    # Kayıt ve Giriş
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), # views.py'da ismini login_view yaptık
    path('logout/', views.logout_view, name='logout'),

    # Profil İşlemleri
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
]