from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'event_added',
                    'tickets_available')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'event_added')
    summernote_fields = ('description')
