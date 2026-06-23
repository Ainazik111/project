from modeltranslation.translator import TranslationOptions, register
from .models import Food, Drink


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Drink)
class DrinkTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
