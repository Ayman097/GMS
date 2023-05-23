from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagedetail/<int:pk>', views.page_detail, name='page'),
    path('faq', views.faq, name='faq'),
    path('inquiry', views.inquiry, name='inquiry'),
]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)