from django.contrib import admin

from django.contrib import admin
from .models import Food, Drink

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

