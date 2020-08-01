from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry, ENTRY_STATUS
from django.http import HttpResponseNotAllowed


def index_view(request):
    entry = Entry.objects.all()
    return render(request, 'index.html', context={'entry': entry})


def entry_view(request, pk):
    pass


def entry_create(request):
    pass


def entry_update(request, pk):
    pass


def entry_delete(request, pk):
    pass