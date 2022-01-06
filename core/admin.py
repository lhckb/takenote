from django.contrib import admin
from core.models import Note

class NotesInAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'user', 'pinned')
    list_filter = ('user',)

admin.site.register(Note, NotesInAdmin)
