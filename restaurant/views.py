from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from restaurant.forms import BookingForm, UserForm, EmailForm
from .models import Menu, Starter, MainDish, Dessert, Event, Booking, Customer
from django.contrib.auth.models import User
from django.contrib import messages

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
        messages.success(request,
                         'Your reservation request has been sent')
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
            messages.success(request,
                             'Your reservation request has been updated')
        return redirect('profile')
    booking = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.warning(request,
                     'Your reservation has been cancelled')
    return redirect('profile')


def edit_username(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = UserForm(instance=user)
    if request.POST:
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile information has been updated')
        return redirect('profile')
    user = UserForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'edit_username.html', context)


def edit_email(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = EmailForm(instance=user)
    if request.POST:
        form = EmailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your email address has been updated')
        return redirect('profile')
    user = EmailForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'edit_email.html', context)


def delete_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.warning(request,
                     'Your Account has been successfully closed')
    return redirect('home')
