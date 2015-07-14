from django.conf.urls import patterns, include, url
from django.contrib import admin
from todos import views

urlpatterns = patterns('',
    url(r'^list/$', views.notes_list, name='notes_list'),
    url(r'^note/(?P<note_id>\d+)$', views.note, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)