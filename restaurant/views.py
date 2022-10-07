from django.shortcuts import render, get_object_or_404
from django.views import generic, View


# Create your views here.


def index(request):
    # Returns the index.html page
    return render(request, "index.html")


def profile(request):
    """
    renders profile page
    """
    return render(request, "profile.html")


def about(request):
    """
    renders about page
    """
    return render(request, "about.html")


def restaurant(request):
    """
    renders restaurant page
    """
    return render(request, "restaurant.html")
