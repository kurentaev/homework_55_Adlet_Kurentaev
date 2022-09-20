from django.shortcuts import render
from webapp.models import TasksList


def index_view(request):
    tasks = TasksList.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, "index.html", context)

