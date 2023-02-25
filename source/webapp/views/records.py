from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import RecordForm
from webapp.models import StatusChoice, Record


def add_view(request: WSGIRequest):
    # GET
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'record_create.html', context={
            'choices': StatusChoice.choices,
            'form': form
        })

    # POST
    form = RecordForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'record_create.html', context={
            'choices': StatusChoice.choices,
            'form': form
        })

    # Success
    else:
        Record.objects.create(**form.cleaned_data)
        return redirect('index')


def update_view(request: WSGIRequest, pk):
    record = get_object_or_404(Record, pk=pk)

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'record_update.html', context={'form': form, 'record': record})

    form = RecordForm(instance=record)
    return render(request, 'record_update.html', context={'form': form, 'record': record})


def delete_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'confirm_delete.html', context={'record': record})


def confirm_delete(request, pk):
    record = Record.objects.get(pk=pk)
    record.delete()
    return redirect('index')