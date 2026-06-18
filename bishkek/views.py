from django.shortcuts import render
from .models import BishkekIntro, Place

def bishkek_intro(request):
    intro = BishkekIntro.objects.all()
    return render(request, 'bishkek/intro.html', {'intro': intro})

def bishkek(request):
    places = Place.objects.all()
    return render(request, 'bishkek/places.html', {'places': places})
