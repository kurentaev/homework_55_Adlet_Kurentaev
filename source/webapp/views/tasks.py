from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import TasksList
from webapp.models import StatusChoices
from webapp.forms import TasksListForm


def add_view(request):
    form = TasksListForm()
    if request.method == "GET":
        return render(request, "task_create.html", context={'choices': StatusChoices.choices, 'form': form})
    form = TasksListForm(request.POST)
    if not form.is_valid():
        return render(request, "task_create.html", context={'choices': StatusChoices.choices, 'form': form})
    # if request.POST.get('deadline') == '':
    #     deadline = None
    # else:
    #     deadline = request.POST.get('deadline')
    # task_data = {
    #     'title': request.POST.get('title'),
    #     'status': request.POST.get('status'),
    #     'deadline': deadline,
    #     'description': request.POST.get('description')
    # }
    # task = TasksList.objects.create(**task_data)
    task = TasksList.objects.create(**form.cleaned_data)
    return redirect('todo_detail', pk=task.pk)


def task_view(request, pk):
    task = get_object_or_404(TasksList, pk=pk)
    return render(request, 'task.html', context={'task': task, "choices": StatusChoices.choices})


def delete_view(request, pk):
    task = get_object_or_404(TasksList, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(TasksList, pk=pk)
    task.delete()
    return redirect('index')


def update_view(request, pk):
    task = get_object_or_404(TasksList, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.author = request.POST.get('status')
        task.text = request.POST.get('deadline')
        task.status = request.POST.get('description')
    return render(
        request,
        'task_update.html',
        context={
            'task': task,
            'choices': StatusChoices.choices
            })
