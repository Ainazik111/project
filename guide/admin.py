from django.contrib import admin
from .models import App, InstagramAccount, Service, EmergencyContact, TravelTip

admin.site.register(App)
admin.site.register(InstagramAccount)
admin.site.register(Service)
admin.site.register(EmergencyContact)
admin.site.register(TravelTip)

