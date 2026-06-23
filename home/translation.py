from modeltranslation.translator import TranslationOptions, register
from .models import HomeInfo, Population, Language, People, NationalGame, MusicalInstrument


@register(HomeInfo)
class HomeInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Population)
class PopulationTranslationOptions(TranslationOptions):
    fields = ('number', 'description')


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(People)
class PeopleTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(NationalGame)
class NationalGameTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(MusicalInstrument)
class MusicalInstrumentTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
