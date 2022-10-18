from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from restaurant.forms import BookingForm
from .models import Menu, Starter, MainDish, Dessert, Event, Booking, Customer
from django.contrib.auth.models import User

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
    menus = Menu.objects.all()
    starters = Starter.objects.all()
    mains = MainDish.objects.all()
    desserts = Dessert.objects.all()
    return render(request, "index.html", {
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
        'menus': menus
    })


def profile(request):
    """
    renders profile page
    """
    bookings = Booking.objects.all()
    return render(request, "profile.html",
                  {'bookings': bookings})


def about(request):
    """
    renders about page
    """
    return render(request, "about.html")


def restaurant(request):
    """
    renders restaurant page
    """
    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profile')

    form = BookingForm(request.POST)
    return render(request, "restaurant.html", {'form': BookingForm})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm(instance=booking)
    if request.POST:
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
        return redirect('profile')
    booking = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)
