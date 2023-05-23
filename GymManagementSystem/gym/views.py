from django.shortcuts import render
from .models import Banners, Service, Pages, Faq
from .forms import InquiryForm

# Create your views here.
def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3] # Fetch only 3

    return render(request, 'home.html', {'banners': banners, 'services': services})

def page_detail(request, pk):
    page = Pages.objects.get(id=pk)
    
    return render(request, 'page.html', {'page': page})

def faq(request):
    faqs = Faq.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

# Inquery
def inquiry(request):
    msg = ''
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been Sended'
    form = InquiryForm(request.POST)
    return render(request, 'inquiry.html', {'form': form, 'msg': msg})