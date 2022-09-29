from django.urls import path

from webapp.views.tasks import add_view
from webapp.views.base import index_view
from webapp.views.tasks import task_view
from webapp.views.tasks import delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('todo_list/add/', add_view, name='todo_add'),
    path('todo_list/', index_view, name='index'),
    path('todo_list/<int:pk>', task_view, name='todo_detail'),
    path('delete_task/<int:pk>', delete_view, name='delete')
]
