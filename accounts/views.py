from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Profile

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        kullanici_adi = request.POST.get('username')
        email_adresi = request.POST.get('email')
        sifre = request.POST.get('password')
        sifre2 = request.POST.get('re_password')

        if not all([kullanici_adi, sifre, sifre2]):
            return render(request, 'accounts/register.html', {'error': 'Lütfen tüm zorunlu alanları doldurun.'})

        if sifre == sifre2:
            try:
                user = User.objects.create_user(username=kullanici_adi, email=email_adresi, password=sifre)
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'accounts/register.html', {'error': 'Bu kullanıcı adı zaten alınmış.'})
        else:
            return render(request, 'accounts/register.html', {'error': 'Şifreler uyuşmuyor.'})

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        kullanici_adi = request.POST.get('username')
        sifre = request.POST.get('password')

        user = authenticate(request, username=kullanici_adi, password=sifre)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'profile'))
        else:
            return render(request, 'accounts/login.html', {'error': 'Kullanıcı adı veya şifre hatalı.'})

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required(login_url='login')
def edit_profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        profile.location = request.POST.get('location')
        profile.bio = request.POST.get('bio')
        
        dogum_tarihi = request.POST.get('birth_date')
        profile.birth_date = dogum_tarihi if dogum_tarihi else None
        
        profile.save()
        return redirect('profile')

    return render(request, 'accounts/edit_profile.html', {'profile': profile})