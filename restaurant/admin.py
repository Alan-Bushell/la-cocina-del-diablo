from django.contrib import admin
from .models import Menu, Starter, MainDish, Dessert
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


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
