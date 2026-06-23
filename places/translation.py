from modeltranslation.translator import TranslationOptions, register
from .models import Place


@register(Place)
class PlaceTranslationOptions(TranslationOptions):
    fields = ('name', 'region', 'description')
