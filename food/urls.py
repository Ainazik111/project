from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_page, name='food'),
]
