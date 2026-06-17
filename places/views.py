from django.shortcuts import render
from .models import Place

def places_page(request):
    places = Place.objects.all()
    return render(request, 'places/places.html', {'places': places})

