from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

# --- 1. KAYIT OLMA (MANUEL) ---
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        kullanici_adi = request.POST.get('username')
        email_adresi = request.POST.get('email')
        sifre = request.POST.get('password')
        sifre2 = request.POST.get('re_password')

        # Şifre Eşleşme Kontrolü
        if sifre == sifre2:
            # Kullanıcı adı dolu mu kontrolü
            if User.objects.filter(username=kullanici_adi).exists():
                return render(request, 'accounts/register.html', {'error': 'Bu kullanıcı adı zaten alınmış.'})
            
            # Kullanıcıyı oluştur
            user = User.objects.create_user(username=kullanici_adi, email=email_adresi, password=sifre)
            
            # KAPSÜLÜ (PROFİLİ) ELLE OLUŞTUR (Sinyal olmadığı için şart)
            Profile.objects.create(user=user)

            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/register.html', {'error': 'Şifreler uyuşmuyor.'})

    return render(request, 'accounts/register.html')

# --- 2. GİRİŞ YAPMA (MANUEL) ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        kullanici_adi = request.POST.get('username')
        sifre = request.POST.get('password')

        user = authenticate(request, username=kullanici_adi, password=sifre)

        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'accounts/login.html', {'error': 'Kullanıcı adı veya şifre hatalı.'})

    return render(request, 'accounts/login.html')
# --- 3. ÇIKIŞ YAPMA ---
def logout_view(request):
    logout(request)
    return redirect('login')

# --- 4. PROFİL GÖRÜNTÜLEME ---
@login_required(login_url='login')
def profile_view(request):
    return render(request, 'accounts/profile.html')

# --- 5. PROFİL DÜZENLEME (MANUEL) ---
@login_required(login_url='login')
def edit_profile_view(request):
    user = request.user
    # Profil kapsülü yoksa (eski üye vb.) hata vermesin diye get_or_create kullanıyoruz
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        # --- User Tablosu Güncelleme ---
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        # --- Profile (Kapsül) Tablosu Güncelleme ---
        profile.location = request.POST.get('location')
        profile.bio = request.POST.get('bio')
        
        dogum_tarihi = request.POST.get('birth_date')
        if dogum_tarihi: # Tarih boş gelirse hata vermemesi için
            profile.birth_date = dogum_tarihi
        else:
            profile.birth_date = None
        
        profile.save()

        return redirect('profile')

    return render(request, 'accounts/edit_profile.html')