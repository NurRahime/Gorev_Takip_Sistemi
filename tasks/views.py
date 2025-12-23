from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

# 1. GÖREV LİSTELEME
#@login_required
def task_list_view(request):
    tasks = Task.objects.all().order_by('-created_at') # En yeniler en üstte
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# 2. GÖREV EKLEME (CREATE)
#@login_required
def task_create_view(request):
    if request.method == "POST":
        # HTML'den verileri çekiyoruz
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        # Tarih boş gelirse hata vermemesi için kontrol
        if not due_date:
            due_date = None

        # Veritabanına Kaydetme
        Task.objects.create(
            title=title,
            description=description,
            status=status,
            due_date=due_date
        )
        return redirect('task_list')

    return render(request, 'tasks/task_form.html')

# 3. GÖREV DÜZENLEME (UPDATE)
#@login_required
def task_update_view(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        # HTML'den gelen yeni verilerle objeyi güncelle
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        
        due_date = request.POST.get('due_date')
        if due_date:
            task.due_date = due_date
        else:
            task.due_date = None
            
        task.save() # Değişiklikleri kaydet
        return redirect('task_list')

    return render(request, 'tasks/task_update.html', {'task': task})
    
# 4. SİLME (OPSİYONEL - URL'e eklersen çalışır)
@login_required
def task_delete_view(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})