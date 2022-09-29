from django.shortcuts import render
from webapp.models import TasksList
from webapp.models import StatusChoices


def index_view(request):
    tasks = TasksList.objects.all()
    context = {
        "tasks": tasks,
        "choices": StatusChoices.choices
    }
    return render(request, "index.html", context)

