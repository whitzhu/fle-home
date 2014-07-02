from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

class UserResource(models.Model):
    category_options = (
        ('user_manual', 'User Manual'),
        ('install_guide', 'Install Guide'),
        ('general',' General'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_options) 
    version = models.CharField(max_length=50, blank=True, help_text="Leave version blank for items categorized as 'General'. Otherwise, put the major.minor version (e.g. '0.11')")
    doc_id = models.CharField(max_length=80, help_text="44-digit ID of the Google Doc")
    filename = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_download_url(self):
        return settings.MEDIA_URL + "user_resources/" + self.filename

    def get_download_path(self):
        return settings.MEDIA_ROOT + "user_resources/" + self.filename

    def get_embed_url(self):
        return "https://docs.google.com/document/d/%s/pub?embedded=true" % self.doc_id

    def get_google_download_url(self):
        return "https://docs.google.com/document/d/%s/export?format=pdf" % self.doc_id

    def clean(self):
        """Ensure version is empty if category is general"""
        if self.category == "general" and self.version != '':
            raise ValidationError("Items in the General category must have a blank version number.")
        elif self.category != "general" and self.version == '':
            raise ValidationError('Version number cannot be blank if resource is a user manual or install guide.')
