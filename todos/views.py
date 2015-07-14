from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Todo

# Create your views here.
def notes_list(request):
    allnotes = Todo.objects.all()
    return render(request, 'notes/index.html', {'notes': allnotes})   

def note(request, note_id):
    note = Todo.objects.get(id=note_id)
    responsetext = ""
    responsetext += "<h1>" + str(note.date) + "</h1>"
    responsetext += "<h3>" + "Todo: " + note.todo + "</h3>"
    return HttpResponse(responsetext)

