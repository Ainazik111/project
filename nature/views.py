from django.shortcuts import render
from .models import NatureArticle

def nature_page(request):
    articles = NatureArticle.objects.all()
    return render(request, 'nature/nature.html', {'articles': articles})
