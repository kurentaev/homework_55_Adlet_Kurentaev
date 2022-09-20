from django.urls import path

from webapp.views.articles import add_view
from webapp.views.base import index_view
from webapp.views.articles import detail_view


urlpatterns = [
    path('', index_view),
    path('articles/add/', add_view),
    path('articles/', detail_view)
]

