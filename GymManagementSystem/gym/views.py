from django.shortcuts import render, redirect
from .models import *
from .forms import InquiryForm, SignUp, ProfileForm, TrainerLoginForm
from django.core.mail import EmailMessage
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import get_template

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

	    success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
	    client_reference_id=plan_id
	)
    
    return redirect(session.url, code=303)

# Success
def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    plan = SubscriptionPlans.objects.get(pk=plan_id)
    user = request.user
    Subscribtion.objects.create(
        plan=plan,
        user=user,
        price=plan.price
    )
    subject = 'Order Email'
    html_content = get_template('orderemail.html').render({'title': plan.title})
    from_email = 'Ayman\'s Gym'
    msg = EmailMessage(subject, html_content, from_email, ['ayman@gmail.com'])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return render(request, 'pay_success.html')

# Cancel
def pay_cancel(request):
	return render(request, 'pay_cancel.html')

# User Dashboard Start

def user_dashboard(request):
    return render(request, 'user/dashboard.html')

def update_profile(request):
    msg = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Data Has been Saved'
    form = ProfileForm(instance=request.user)
    return render(request, 'user/edit_profile.html', {'form': form, 'msg': msg})

# Trainer Login
def trainer_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        trainers = Trainer.objects.filter(username=username, password=password).count()
        if trainers > 0:
            request.session['trainerLogin'] = True
            return redirect('/trainer_dashboard')
        else:
            msg = "Invalid!!"
        
    form = TrainerLoginForm(request.POST)
    return render(request, 'trainer/login.html', {'form': form, 'msg': msg})

# Trainer Logout
def trainer_logout(request):
    del request.session['trainerLogin']
    return redirect('home')

def notification(request):
    data = Notify.objects.all().order_by('-id')
    return render(request, 'notify.html', {'data': data})

def get_notify(request):
    data = Notify.objects.all().order_by('-id')
    jsonData = serializers.serialize('json', data)

    return JsonResponse({'data': jsonData})

