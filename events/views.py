from django.shortcuts import render

# Create your views here.
from .models import Event
from django.utils import timezone

def upcoming_events(request):
       events = Event.objects.filter(date__gte=timezone.now()).union(
           Event.objects.filter(date__lt=timezone.now(), date__gte=timezone.now() - timezone.timedelta(days=7))
       ).order_by('date')

       return render(request, 'upcoming_events.html', {'events': events})