from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# Banners
class Banners(models.Model):
    img = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="100" /> ')


# Services
class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='services/', null=True)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="100" /> ')

# Pages (About Us & Privacy & Terms)
class Pages(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()

    class Meta:
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.title
# FAQ  
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

# Inquery Form
class Inquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# Gallery
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='gallery/', null=True)

    class Meta:
        verbose_name_plural = 'gallery'

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url) )
    
# GalleryImage
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    alt_text = models.CharField(max_length=150)
    img = models.ImageField(upload_to='gallery_imgs/', null=True)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url) )
    
# Subscription Plans
class SubscriptionPlans(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    max_member = models.IntegerField(null = True, blank= True)
    highlight_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Subscription Plans'
    
# Pricing Plane Feature
class SubscriptionPlansFeature(models.Model):
    pricing = models.ManyToManyField(SubscriptionPlans)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# Subscription Discount
class PlanDiscount(models.Model):
    subplan = models.ForeignKey(SubscriptionPlans, on_delete= models.CASCADE, null= True)
    total_months = models.IntegerField()
    total_discount = models.IntegerField()

    def __str__(self):
        return str(self.total_months)
    
# User Subscriber
class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    mobile = models.IntegerField()
    address = models.TextField()
    user_img = models.ImageField(upload_to='user_imgs/', null= True)

    def __str__(self):
        return self.user

    def image_tag(self):
        if self.user_img:
            return mark_safe(f'<img src="{self.user_img.url}" width="100" /> ')
        else:
            return 'No Image'

@receiver(post_save, sender = User)
def create_subscriber(sender, instance, created, **kwargs):
    if created:
        Subscriber.objects.create(user=instance)
    
class Subscribtion(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    plan = models.ForeignKey(SubscriptionPlans, on_delete= models.CASCADE, null= True)
    price = models.IntegerField()

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.TextField()
    is_active = models.BooleanField(default=False)
    detail = models.TextField()
    trainer_img = models.ImageField(upload_to='trainers/')

    def __str__(self):
        return self.name
    
    def image_tag(self):
        if self.trainer_img:
            return mark_safe(f'<img src="{self.trainer_img.url}" width="100" /> ')
        else:
            return 'No Image'

