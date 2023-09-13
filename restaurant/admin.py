from django.contrib import admin
from .models import Menu, Starter, MainDish, Dessert, Event, Booking, Customer
from django_summernote.admin import SummernoteModelAdmin


# Events
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'event_added',
                    'tickets_available')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'event_added')
    summernote_fields = ('description')


# Bookings
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('id', 'customer', 'booking_date', 'booking_time',
                'number_of_attendees', 'booking_status')
    search_fields = ['id', 'customer', 'booking_date', 'booking_time', 'booking_status']
    list_filter = ('booking_status', 'booking_date')


# Customers
@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):

    list_display = ('user', 'first_name', 'last_name', 'email',
                    'contact_phone')
    search_fields = ['user', 'email', 'contact_phone', 'last_name']


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'image', 'description',
                    'set_menu', 'price', 'status', 'date_created')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'date_created')
    summernote_fields = ('description')


# Starters
@admin.register(Starter)
class StarterAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'price', 'menu')
    search_fields = ['title', 'description']
    list_filter = ('title', 'price')
    summernote_fields = ('description')


# Main Dish
@admin.register(MainDish)
class MainDishAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'price', 'menu')
    search_fields = ['title', 'description']
    list_filter = ('title', 'price')
    summernote_fields = ('description')


# Desserts
@admin.register(Dessert)
class DessertAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'price', 'menu')
    search_fields = ['title', 'description']
    list_filter = ('title', 'price')
    summernote_fields = ('description')
