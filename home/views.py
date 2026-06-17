from django.shortcuts import render
from .models import HomeInfo, Population, Language, People, NationalGame, MusicalInstrument

def home_page(request):
    info = HomeInfo.objects.all()
    population = Population.objects.all()
    languages = Language.objects.all()
    people = People.objects.all()
    games = NationalGame.objects.all()
    instruments = MusicalInstrument.objects.all()

    return render(request, 'home/home.html', {
        'info': info,
        'population': population,
        'languages': languages,
        'people': people,
        'games': games,
        'instruments': instruments
    })

