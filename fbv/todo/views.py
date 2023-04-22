# Function Based Views
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET
from .forms import TaskForm, ConfirmForm
from .models import Task


@require_GET
@cache_page(60)
def task_list_view(request):
    return render(request, 'todo/task_list.html', {
        'tasks': Task.objects.all(),
    })


@login_required
@require_http_methods(["GET", "POST"])
def task_create_view(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        return redirect('task-detail', pk=task.pk)
    return render(request, 'todo/task_create.html', {
        'form': form,
    })


@require_GET
def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render(request, 'todo/task_detail.html', {
        'task': task,
    })

@login_required
@require_http_methods(["GET", "POST"])
def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=task.pk)

    return render(request, 'todo/task_update.html', {
        'task': task,
        'form': TaskForm(instance=task),
    })

@login_required
@require_http_methods(["GET", "POST"])
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = ConfirmForm(data=request.POST)
        if form.is_valid():
            task.delete()
            return redirect('task-list')

    return render(request, 'todo/task_confirm_delete.html', {
        'task': task,
        'form': ConfirmForm(),
    })
