from django.shortcuts import render

from webapp.models import Record, StatusChoice


# Create your views here.


def index_view(request):
    records = Record.objects.order_by('-created_at').exclude(status='blocked')
    context = {'records': records}
    return render(request, 'index.html', context=context)