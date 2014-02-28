from django.db import models
from markupfield.fields import MarkupField

# Create your models here.
class AboutSection(models.Model):
	title = models.CharField(max_length=200)
	body = MarkupField()