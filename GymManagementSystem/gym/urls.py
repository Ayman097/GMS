from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagedetail/<int:pk>', views.page_detail, name='page'),
    path('faq', views.faq, name='faq'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery_img/<int:pk>', views.gallery_detail, name='gallery_img'),
    path('pricing', views.pricing, name='pricing'),
    path('accounts/signup', views.signup, name='signup'),
    path('checkout/<int:plan_id>', views.checkout, name='checkout'),
    path('checkout_session/<int:plan_id>', views.checkout_session, name='checkout_session'),
    path('pay_success', views.pay_success, name='pay_success'),
    path('pay_cancel', views.pay_cancel, name='pay_cancel'),
    
]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)