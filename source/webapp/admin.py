from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('pk', 'author', 'description', 'status', 'created_at', 'updated_at')
    list_display_links = ('pk', 'author')
    search_fields = ('author',)


admin.site.register(Entry, EntryAdmin)