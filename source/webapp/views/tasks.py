from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import TasksList


def add_view(request):
    if request.method == "GET":
        return render(request, "task_create.html")
    if request.POST.get('deadline') == '':
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
    return render(request, 'task.html', context={'task': task})


def delete_view(request, pk):
    task = get_object_or_404(TasksList, pk=pk)
    task.delete()
    return redirect('/')
