from modeltranslation.translator import TranslationOptions, register
from .models import App, InstagramAccount, Service, EmergencyContact, TravelTip


@register(App)
class AppTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(InstagramAccount)
class InstagramAccountTranslationOptions(TranslationOptions):
    fields = ('username', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(EmergencyContact)
class EmergencyContactTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(TravelTip)
class TravelTipTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
