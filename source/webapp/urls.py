from django.urls import path

from source.webapp.views.views import index_view

urlpatterns = [
    path('', index_view, name='index')
]