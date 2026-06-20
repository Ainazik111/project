from django.urls import path
from . import views

urlpatterns = [
    path('', views.bishkek_intro, name='bishkek_intro'),
    path('places/', views.bishkek, name='bishkek'),
]
