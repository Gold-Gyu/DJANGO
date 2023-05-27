from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source = "image", processors=[Thumbnail(100, 100)], options = {'quality':90})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

