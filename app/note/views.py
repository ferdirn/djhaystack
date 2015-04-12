from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from app.note.models import Note


class IndexView(generic.ListView):
    template_name = 'note/index.html'
    context_object_name = 'latest_notes'

    def get_queryset(self):
        """ return latest notes """
        return Note.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Note
    template_name = 'note/detail.html'

    def get_queryset(self):
        """ return latest notes """
        return Note.objects.filter(pub_date__lte=timezone.now())

