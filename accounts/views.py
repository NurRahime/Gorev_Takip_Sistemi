from django.shortcuts import render, redirect

def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    return redirect('login')

def profile_view(request):
    return render(request, 'accounts/profile.html')

def edit_profile_view(request):
    return render(request, 'accounts/edit_profile.html')