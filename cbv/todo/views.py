# Class Based Viwes
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import TaskForm, ConfirmForm
from .models import Task

class TaskBaseView(View):
    def get_task(self, pk):
        task = get_object_or_404(Task, pk=pk)
        return task

class TaskListView(TaskBaseView):

    def get(self, request, *args, **kwargs):
        return render(request, 'todo/task_list.html', {
            'tasks': Task.objects.all(),
        })

class TaskCreateView(LoginRequiredMixin, TaskBaseView):

    def get(self, request, *args, **kwargs):
        return render(request, 'todo/task_create.html', {
            'form': TaskForm(),
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task-detail', pk=task.pk)

        return self.get(request)


class TaskDetailView(TaskBaseView):

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)

        return render(request, 'todo/task_detail.html', {
            'task': task,
        })


class TaskUpdateView(LoginRequiredMixin, TaskBaseView):

    def get(self, request, pk, *args, **kwargs):
        task = self.get_task(pk)
        return render(request, 'todo/task_update.html', {
            'task': task,
            'form': TaskForm(instance=task),
        })

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=task.pk)

        return self.get(request, pk)


class TaskDeleteView(LoginRequiredMixin, TaskBaseView):

    def get(self, request, pk, *args, **kwargs):
        task = self.get_task(pk)
        return render(request, 'todo/task_confirm_delete.html', {
            'task': task,
            'form': ConfirmForm(),
        })

    def post(self, request, pk, *args, **kwargs):
        task = self.get_task(pk)
        form = ConfirmForm(data=request.POST)
        if form.is_valid():
            task.delete()
            return redirect('task-list')

        return self.get(request, pk)
