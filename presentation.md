- [Принцип DRY](#org96101c3)
- [Декораторы](#org8c612e7)
- [Декораторы в Django](#org424f4db)
- [Function Based View](#org617c661)
- [Class Based View](#org0cc1e99)
- [Generic Based View](#org02d00f5)
- [Схема выбора](#orgd0b9cbf)
- [Дополнительная литература](#org05bf791)



<a id="org96101c3"></a>

# Принцип DRY

-   **D:** on't  
    *не*
-   **R:** epeat  
    *повторяй*
-   **Y:** ourself  
    *-ся*


<a id="org8c612e7"></a>

# Декораторы

```python
C = Callable[[Any], Any]
Callable[[C], C]
```


<a id="org424f4db"></a>

# Декораторы в Django

<https://docs.djangoproject.com/en/4.2/topics/http/decorators/>  


<a id="org617c661"></a>

# Function Based View

```python
# Function Based Views
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, ConfirmForm
from .models import Task


def task_list_view(request):
    return render(request, 'todo/task_list.html', {
        'tasks': Task.objects.all(),
    })


def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task-detail', pk=task.pk)

    return render(request, 'todo/task_create.html', {
        'form': TaskForm(),
    })


def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render(request, 'todo/task_detail.html', {
        'task': task,
    })


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
```


<a id="org0cc1e99"></a>

# Class Based View

```python
# Class Based Viwes
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import TaskForm, ConfirmForm
from .models import Task


class TaskListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'todo/task_list.html', {
            'tasks': Task.objects.all(),
        })


class TaskCreateView(View):

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


class TaskDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)

        return render(request, 'todo/task_detail.html', {
            'task': task,
        })


class TaskUpdateView(View):

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
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


class TaskDeleteView(View):

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'todo/task_confirm_delete.html', {
            'task': task,
            'form': ConfirmForm(),
        })

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = ConfirmForm(data=request.POST)
        if form.is_valid():
            task.delete()
            return redirect('task-list')

        return self.get(request, pk)
```


<a id="org02d00f5"></a>

# Generic Based View

```python
# Generic Based Views
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    context_object_name = 'task'
    fields = ('name', 'description', 'is_done')
    template_name = 'todo/task_create.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    fields = ('name', 'description', 'is_done')
    template_name = 'todo/task_update.html'


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/'
```


<a id="orgd0b9cbf"></a>

# Схема выбора

![img](flowchart.png)  


<a id="org05bf791"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[Python Design Patterns](https://python-patterns.guide/)</span></span>
-   <span class="underline"><span class="underline">[Blog](https://testdriven.io/blog/django-class-based-vs-function-based-views/)</span></span>
-   <span class="underline"><span class="underline">[Mixins](https://django.fun/ru/docs/django/4.0/topics/class-based-views/mixins/)</span></span>
