from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='events'),
    path('<slug:slug>', views.EventDetail.as_view(), name='event_detail'),
    path('events/', views.events, name='events'),
]
