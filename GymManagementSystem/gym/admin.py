from django.contrib import admin
from .models import Banners, Service

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
admin.site.register(Banners, BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Service, ServiceAdmin)