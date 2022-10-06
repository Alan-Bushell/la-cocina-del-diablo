from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event


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


def profile(request):
    """
    renders profile page
    """
    return render(request, "profile.html")


def events(request):

    return render(request, "events.html")
