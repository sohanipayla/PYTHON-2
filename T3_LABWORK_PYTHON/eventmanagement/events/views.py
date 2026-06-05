from django.shortcuts import render
from .models import Event

def home(request):
    return render(request, 'events/home.html')

def upcoming_events(request):
    events = Event.objects.all().order_by('date')
    search_query = request.GET.get('search', '')
    return render(request, 'events/upcoming.html', {'events': events, 'search_query': search_query})
