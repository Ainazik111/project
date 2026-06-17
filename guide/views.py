from django.shortcuts import render

from django.shortcuts import render
from .models import App, InstagramAccount, Service, EmergencyContact, TravelTip

def guide_page(request):
    apps = App.objects.all()
    instagrams = InstagramAccount.objects.all()
    services = Service.objects.all()
    contacts = EmergencyContact.objects.all()
    tips = TravelTip.objects.all()
    return render(request, 'guide/guide.html', {
        'apps': apps,
        'instagrams': instagrams,
        'services': services,
        'contacts': contacts,
        'tips': tips
    })

