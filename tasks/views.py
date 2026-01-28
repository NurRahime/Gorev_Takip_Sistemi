from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

@login_required
def task_list_view(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        if not due_date:
            due_date = None

        Task.objects.create(
            title=title,
            description=description,
            status=status,
            due_date=due_date
        )
        
        messages.success(request, 'Yeni görev başarıyla oluşturuldu.')
        return redirect('task_list')

    return render(request, 'tasks/task_create.html')

@login_required
def task_update_view(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        if due_date:
            task.due_date = due_date
        else:
            task.due_date = None
            
        task.save()
        
        messages.success(request, 'Görev detayları güncellendi.')
        return redirect('task_list')

    return render(request, 'tasks/task_update.html', {'task': task})

@login_required
def task_delete_view(request, id):
    task = get_object_or_404(Task, id=id)
    
    if request.method == "POST":
        task.delete()
        messages.error(request, 'Görev silindi.')
        return redirect('task_list')
    
    return redirect('task_list')