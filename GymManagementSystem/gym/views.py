from django.shortcuts import render
from .models import Banners, Service

# Create your views here.
def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3] # Fetch only 3

    return render(request, 'home.html', {'banners': banners, 'services': services})
