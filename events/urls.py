from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>', views.EventDetail.as_view(), name='event_detail'),
    path('profile/', views.profile, name='profile'),
    path('events/', views.events, name='events'),
]
