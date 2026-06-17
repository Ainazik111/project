from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'category')
    search_fields = ('name', 'region')
    list_filter = ('region', 'category')

