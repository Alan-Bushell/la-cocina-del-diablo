from django.contrib import admin
from .models import Menu, Starter, MainDish, Dessert, Event
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


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'image', 'description',
                    'set_menu', 'price', 'status', 'date_created')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'date_created')
    summernote_fields = ('description')


@admin.register(Starter)
class StarterAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'price')
    search_fields = ['title', 'description']
    list_filter = ('title', 'price')
    summernote_fields = ('description')


@admin.register(MainDish)
class MainDishAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'price')
    search_fields = ['title', 'description']
    list_filter = ('title', 'price')
    summernote_fields = ('description')


@admin.register(Dessert)
class DessertAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'price')
    search_fields = ['title', 'description']
    list_filter = ('title', 'price')
    summernote_fields = ('description')
