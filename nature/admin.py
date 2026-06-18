from django.contrib import admin
from .models import NatureArticle, NatureContent

class NatureContentInline(admin.TabularInline):
    model = NatureContent
    extra = 1

@admin.register(NatureArticle)
class NatureArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [NatureContentInline]

