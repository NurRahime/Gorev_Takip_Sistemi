# Create your views here.
from django.shortcuts import render, redirect

def arcihve(request):
    return render(request, 'archive/archive.html')


def notifications(request):
    return render(request, 'archive/notifications.html')