from django.urls import path

from webapp.views.base import index_view
from webapp.views.records import add_view, update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('record/add', add_view, name='record_add'),
    path('article/<int:pk>/update/', update_view, name='record_update')
]