from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from .models import Notification

def archive_view(request):
    query = request.GET.get('q')
    # Senin özel çalışan satırın
    archived_tasks = Task.objects.filter(status__icontains='Tamam')
    
    if query:
        archived_tasks = archived_tasks.filter(title__icontains=query)
    
    context = {
        'tasks': archived_tasks,
        'query': query,
    }
    return render(request, 'archive/archive.html', context)

def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'archive/notifications.html', {'notifications': notifications})

def mark_as_read(request, notification_id):
    # Bu fonksiyon urls.py'deki hata alan 'mark_as_read' kısmını düzeltecek
    notification = get_object_or_404(Notification, id=notification_id)
    notification.read = True
    notification.save()
    return redirect('notifications_list')