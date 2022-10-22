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
    path('delete_account/<user_id>', views.delete_account,
         name='delete_account'),
    path('edit_username/<user_id>', views.edit_username, name='edit_username'),
    path('edit_email/<user_id>', views.edit_email, name='edit_email'),
    path('edit_profile/<user_id>', views.edit_profile,
         name='edit_profile'),
    path('events/', views.EventList.as_view(), name='events'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
