from django.contrib import admin
from .models import Place


admin.site.register(Place)
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
