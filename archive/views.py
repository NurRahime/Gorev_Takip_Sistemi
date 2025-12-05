from django.shortcuts import render, redirect

def archive(request):
    return render(request, 'archive/archive.html')


def notifications(request):
    return render(request, 'archive/notifications.html')