from django.db import models
from django.utils.html import mark_safe
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