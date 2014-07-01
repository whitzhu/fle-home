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
    version = models.CharField(max_length=50, blank=True, help_text="Leave version blank for items categorized as 'General'")
    doc_url = models.URLField(max_length=200)
    pdf_url = models.URLField(max_length=200, help_text="Publish the PDF to a public Dropbox folder.")
    slug = models.SlugField(max_length=50, unique=True)
    publish_date = models.DateTimeField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.title

    def clean(self):
        """Ensure version is empty if category is general"""
        if self.category == "general" and self.version != '':
            raise ValidationError("Items in the General category must have a blank version number.")
        elif self.category != "general" and self.version == '':
            raise ValidationError('Version number cannot be blank if resource is a user manual or install guide.')


class DeploymentStory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField(help_text="In degrees, South is negative!")
    longitude = models.FloatField(help_text="In degrees, West is negative!")