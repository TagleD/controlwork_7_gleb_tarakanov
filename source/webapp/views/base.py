from django.shortcuts import render

from webapp.models import Record, StatusChoice


# Create your views here.


def index_view(request):
    records = Record.objects.exclude(status=StatusChoice.ACTIVE[0]).order_by('created_at')
    context = {'records': records}
    return render(request, 'index.html', context=context)