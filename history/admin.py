from django.contrib import admin
from .models import Epoch, Event, Culture

@admin.register(Epoch)
class EpochAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    search_fields = ('title', 'year')

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')
    search_fields = ('category', 'name')

