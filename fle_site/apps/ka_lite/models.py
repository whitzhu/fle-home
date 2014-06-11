from django.db import models
from django.template.defaultfilters import slugify

class UserResource(models.Model):
    category_options = (
        ('User Manaual', 'User Manual'),
        ('Install Guide', 'Install Guide'),
        ('General',' General'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_options) 
    version = models.CharField(max_length=50)
    doc_url = models.URLField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    publish_date = models.DateTimeField(auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=True)