from django.shortcuts import render
from .models import HomeInfo, Population, Language, NationalGame

def home_page(request):
    info = HomeInfo.objects.all()
    population = Population.objects.all()
    languages = Language.objects.all()
    games = NationalGame.objects.all()

    return render(request, 'home/index.html', {
        'info': info,
        'population': population,
        'languages': languages,
        'games': games,
    })

