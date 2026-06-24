from django.contrib import admin
from .models import Place
from .models import BishkekIntro

@admin.register(BishkekIntro)
class BishkekIntroAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )

    list_filter = (
        'category',
    )
