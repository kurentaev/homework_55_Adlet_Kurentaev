from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import TasksList
from webapp.models import StatusChoices
from webapp.forms import TasksListForm


def add_view(request):
    if request.method == "GET":
        form = TasksListForm()
        return render(request, "task_create.html", context={'choices': StatusChoices.choices, 'form': form})
    elif request.method == "POST":
        form = TasksListForm(request.POST)
        if form.is_valid():
            if request.POST.get('deadline') == '':
                print(123)
                deadline = None
            else:
                deadline = request.POST.get('deadline')
            task_data = {
                'title': request.POST.get('title'),
                'status': request.POST.get('status'),
                'deadline': deadline,
                'description': request.POST.get('description')
            }
            task = TasksList.objects.create(**task_data)
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
    errors = {}
    task = get_object_or_404(TasksList, pk=pk)
    if request.method == 'GET':
        form = TasksListForm(initial={
            'title': task.title,
            'status': task.status,
            'deadline': task.deadline,
            'description': task.description
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        if request.POST.get('deadline') == '':
            deadline = None
        else:
            deadline = request.POST.get('deadline')
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.deadline = deadline
        task.description = request.POST.get('description')
        if errors:
            return render(
                request,
                'task_update.html',
                context={
                    'task': task,
                    'choices': StatusChoices.choices,
                    'errors': errors
                    })
        task.save()
        return redirect('todo_detail', pk=task.pk)
    return render(
        request,
        'task_update.html',
        context={
            'task': task,
            'choices': StatusChoices.choices
            })
