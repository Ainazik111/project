from django.shortcuts import render
from .models import App, InstagramAccount, EmergencyContact, TravelTip

def guide_page(request):
    apps = App.objects.all()
    instagrams = InstagramAccount.objects.all()
    contacts = EmergencyContact.objects.all()
    tips = TravelTip.objects.all()
    return render(request, 'guide/guide.html', {
        'apps': apps,
        'instagrams': instagrams,
        'contacts': contacts,
        'tips': tips
    })

