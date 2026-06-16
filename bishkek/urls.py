from django.urls import path
from .views import bishkek
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', bishkek, name='bishkek'),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)