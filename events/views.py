from django.shortcuts import render
from .models import Event

def get_events(request):
    events=Event.objects.all()
    return render(request,'events.html',{'events':events})
