from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from restaurant.forms import BookingForm
from .models import Menu, Starter, MainDish, Dessert, Event

# Create your views here.


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-event_added')
    template_name = 'events.html'
    paginate_by = 5


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
            })


class StarterList(generic.ListView):
    model = Starter
    queryset = Starter.objects.get
    template_name = 'index.html'
    paginate_by = 5

    def __str__(self):
        return self.title


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

    context = {'form': BookingForm()}
    return render(request, "restaurant.html", context)
