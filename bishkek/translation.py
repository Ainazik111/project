from modeltranslation.translator import TranslationOptions, register
from .models import BishkekIntro, Place


@register(BishkekIntro)
class BishkekIntroTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Place)
class PlaceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address')
