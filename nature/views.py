from django.shortcuts import render
from .models import Nature

def nature_page(request):
    items = Nature.objects.all()
    return render(request, 'nature/nature.html', {'items': items})

