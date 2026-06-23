from modeltranslation.translator import TranslationOptions, register
from .models import NatureArticle, NatureContent


@register(NatureArticle)
class NatureArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'main_description')


@register(NatureContent)
class NatureContentTranslationOptions(TranslationOptions):
    fields = ('text',)
