from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>', views.delete_booking,
         name='delete_booking'),
    path('events/', views.EventList.as_view(), name='events'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
