from django.shortcuts import render

# Create your views here.
def task_form_view(request):
    return render(request, 'tasks/task_form.html')

def task_list_view(request):
    return render(request,'tasks/task_list.html')

