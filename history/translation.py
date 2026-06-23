from modeltranslation.translator import TranslationOptions, register
from .models import Epoch, Event, Culture


@register(Epoch)
class EpochTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Culture)
class CultureTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
