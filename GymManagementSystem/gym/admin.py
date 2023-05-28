from django.contrib import admin
from .models import Banners, Service, Pages, Faq, Inquiry, Gallery, GalleryImage, SubscriptionPlans, SubscriptionPlansFeature, PlanDiscount

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
admin.site.register(Banners, BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Service, ServiceAdmin)

class PagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Pages, PagesAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)
admin.site.register(Faq, FaqAdmin)

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message', 'send_time')
admin.site.register(Inquiry, InquiryAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Gallery, GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
admin.site.register(GalleryImage, GalleryImageAdmin)

class SubscriptionPlansAdmin(admin.ModelAdmin):
    list_editable = ('highlight_status', 'max_member')
    list_display = ('title', 'price', 'max_member', 'highlight_status')
admin.site.register(SubscriptionPlans, SubscriptionPlansAdmin)

class SubscriptionPlansFeatureAdmin(admin.ModelAdmin):
    list_display=('title','subplans')
    def subplans(self,obj):
        return " | ".join([sub.title for sub in obj.pricing.all()])
admin.site.register(SubscriptionPlansFeature, SubscriptionPlansFeatureAdmin)

class PlanDiscountAdmin(admin.ModelAdmin):
    list_editable = ('total_months', 'total_discount')
    list_display = ('subplan', 'total_months', 'total_discount')
admin.site.register(PlanDiscount, PlanDiscountAdmin)