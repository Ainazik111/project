from django.shortcuts import render
from .models import Food, Drink

def food_page(request):
    foods = Food.objects.all()
    drinks = Drink.objects.all()
    return render(request, 'food/food.html', {
        'foods': foods,
        'drinks': drinks
    })

