from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry, ENTRY_STATUS
from django.http import HttpResponseNotAllowed
from webapp.forms import EntryForm


def index_view(request):
    entry = Entry.objects.filter(status='active').order_by('-created_at')
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
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = EntryForm(initial={'author': entry.author,
                                  'email': entry.email,
                                  'description': entry.description,
                                  'status': entry.status})
        return render(request, 'entry_update.html', context={'form': form, 'entry': entry})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.author = form.cleaned_data['author']
            entry.email = form.cleaned_data['email']
            entry.description = form.cleaned_data['description']
            entry.status = form.cleaned_data['status']
            entry.save()
            return redirect('index')
        else:
            return render(request, 'entry_update.html',
                          context={'form': form,
                                   'entry': entry})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        return render(request, 'entry_delete.html', context={'entry': entry})
    elif request.method == 'POST':
        entry.delete()
        return redirect('index')