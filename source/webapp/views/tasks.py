from django.shortcuts import render, redirect

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
    TasksList.objects.create(**task_data)
    return redirect('/')
