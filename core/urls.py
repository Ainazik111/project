from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('bishkek/', include('bishkek.urls')),
    path('history/', include('history.urls')),
    path('food/', include('food.urls')),
    path('guide/', include('guide.urls')),
    path('nature/', include('nature.urls')),
    path('places/', include('places.urls')),
    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
