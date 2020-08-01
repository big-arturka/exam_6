from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry, ENTRY_STATUS
from django.http import HttpResponseNotAllowed
from webapp.forms import EntryForm


def index_view(request):
    entry = Entry.objects.all()
    return render(request, 'index.html', context={'entry': entry})


def entry_create(request):
    if request.method == 'GET':
        return render(request, 'entry_create.html',
                      context={'form': EntryForm()})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            Entry.objects.create(**form.cleaned_data)
            return redirect('index')
        else:
            return render(request, 'entry_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def entry_update(request, pk):
    pass


def entry_delete(request, pk):
    pass