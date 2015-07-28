from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Note
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from todos.forms import NoteForm
from django.conf.urls import url
from django.db.models import Q


def notes_list(request, folder):
    if folder == "":
        allnotes = Note.objects.all().order_by("folder__title")
        total = allnotes.count()
    else:
        allnotes = Note.objects.filter(folder__title__iexact=folder)
        total = allnotes.count();
    return render(request, 'todos/index.html', {'notes': allnotes, 'total':total})  

def notes_tags(request, tags):
    pieces = tags.split('/')
    for p in pieces:
        queries = [Q(tag__title__iexact=value) for value in pieces]
        query = queries.pop()
        for item in queries:
            query |= item
        allnotes = Note.objects.filter(query).distinct().order_by('folder__title')
        total = allnotes.count();
    return render(request, 'todos/index.html', {'pieces':pieces, 'notes': allnotes, 'total':total})   

def note(request, note_id):
    note = Note.objects.get(id=note_id)   
    return render(request, 'todos/note.html', {'note':note})
    
class NoteList(ListView):
    #https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-display/
    model = Note
    
    def get_queryset(self):
        folder = self.kwargs['folder']
        if folder == '':
            return Note.objects.all()
        else:
            return Note.objects.filter(folder__title__iexact=folder)


class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    
class NoteDetail(DetailView):
    model = Note

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy("todo_listall")



    
    
    