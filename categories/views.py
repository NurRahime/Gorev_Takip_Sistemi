from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')

    return render(request, "categories/categories.html", {
        "categories": categories,
        "form": form
    })
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_list')
def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')

    return render(request, 'categories/edit_category.html', {'form': form})
