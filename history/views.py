from django.shortcuts import render
from .models import Epoch, Event, Culture

def history_page(request):
    epochs = Epoch.objects.all()
    events = Event.objects.all()
    cultures = Culture.objects.all()
    return render(request, 'history/history.html', {
        'epochs': epochs,
        'events': events,
        'cultures': cultures
    })
