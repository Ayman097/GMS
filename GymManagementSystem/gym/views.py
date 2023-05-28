from django.shortcuts import render, redirect
from .models import Banners, Service, Pages, Faq, Gallery, GalleryImage, SubscriptionPlans, SubscriptionPlansFeature
from .forms import InquiryForm, SignUp
import stripe

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
    pricing = SubscriptionPlans.objects.all().order_by('price')
    features = SubscriptionPlansFeature.objects.all()
    
    return render(request, 'pricing.html', {'plans': pricing, 'features': features})

# Sign Up
def signup(request):
    msg = ''
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            msg = "Thanks For Registration"
            
    form = SignUp

    return render(request, 'registration/signup.html', {'form':form, 'msg': msg})

# Check Out
def checkout(request, plan_id):
    plandetail = SubscriptionPlans.objects.get(pk=plan_id)

    return render(request, 'checkout.html', {'plan': plandetail })

stripe.api_key = 'sk_test_51NCaD9DagQuIrgPNsnbjNpTndzXiQrEsCi2sgrzKczF2uoQYUa6PCCw83sjeTtFKhPv4mQxVjDgrYBXhMEVp3Vt400TpBZLGiQ'
def checkout_session(request, plan_id):
    plan= SubscriptionPlans.objects.get(pk=plan_id)
    session=stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
	      'price_data': {
	        'currency': 'usd',
	        'product_data': {
	          'name': plan.title,
	        },
	        'unit_amount': int(plan.price),
	      },
	      'quantity': 1,
	    }],
	    mode='payment',

	    #success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
	    #cancel_url='http://127.0.0.1:8000/pay_cancel',
        success_url='http://127.0.0.1:8000/pay_success',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
	    client_reference_id=plan_id
	)
    return redirect(session.url, code=303)

# Success
def pay_success(request):
	return render(request, 'pay_success.html')

# Cancel
def pay_cancel(request):
	return render(request, 'pay_cancel.html')

