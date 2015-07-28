from django.contrib import admin
from .models import Note, Folder, Tag

class NoteInline(admin.StackedInline): 
    model = Note
    fields = ('title',) 
    extra = 0
    
class FolderAdmin(admin.ModelAdmin):
    inlines = [NoteInline,]
    
    model = Folder

class TaggedNoteInline(admin.TabularInline): 
    model = Note.tag.through
    extra = 0
    
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedNoteInline,]
    model = Tag

admin.site.register(Note)
admin.site.register(Tag, TagAdmin)
admin.site.register(Folder, FolderAdmin)
