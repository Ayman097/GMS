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



class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='services/', null=True)

    class Meta:
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="100" /> ')
