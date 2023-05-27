from django.shortcuts import render
from .models import Banners, Service, Pages, Faq, Gallery, GalleryImage, SubscriptionPlans, SubscriptionPlansFeature
from .forms import InquiryForm

# Create your views here.
def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3] # Fetch only 3
    galleryImgs = GalleryImage.objects.all().order_by('-id')[:9]

    return render(request, 'home.html', {'banners': banners, 'services': services, 'galleryImgs': galleryImgs})

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

# Show galleries
def gallery(request):
    galleries = Gallery.objects.all().order_by('-id') # descending
    return render(request, 'gallery.html', {'galleries': galleries})

# Show galleries
def gallery_detail(request,pk):
    gallery = Gallery.objects.get(id=pk)
    gallery_imgs = GalleryImage.objects.filter(gallery=gallery)
    return render(request, 'gallery_img.html', {'gallery_imgs': gallery_imgs, 'gallery': gallery})

# Pricing
def pricing(request):
    pricing = SubscriptionPlans.objects.all()
    features = SubscriptionPlansFeature.objects.all()
    print(pricing)
    return render(request, 'pricing.html', {'plans': pricing, 'features': features})

