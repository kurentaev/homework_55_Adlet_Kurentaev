from django.urls import path

from webapp.views.articles import add_view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('todo_list/add/', add_view)
]
