from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib import admin
from todos import views
from todos.models import Note

urlpatterns = patterns('',
    url(r'^listall/$', ListView.as_view(model=Note)),
    url(r'^list/(?P<folder>.*)$', views.NoteList.as_view(), name='notes_list'),\
    url(r'^add/$', views.NoteCreate.as_view(), name='note_add'),
    url(r'^note/(?P<pk>\d+)/edit/$', views.NoteUpdate.as_view(),  name='note_update'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.NoteDelete.as_view(),  name='todo_delete'),
    url(r'^note/(?P<pk>\d+)$', views.NoteDetail.as_view(),  name='detail'),
)


