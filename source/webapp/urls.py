from django.urls import path
from webapp.views.base import index_view
from webapp.views.records import add_view, update_view, confirm_delete, delete_view


urlpatterns = [
    path('', index_view, name='index'),
    path('record/add', add_view, name='record_add'),
    path('record/<int:pk>/update/', update_view, name='record_update'),
    path('record/<int:pk>/delete/', delete_view, name='record_delete'),
    path('record/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete')
]