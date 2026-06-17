from django.urls import path
from . import views

urlpatterns = [
    path('', views.nature_page, name='nature'),
]
