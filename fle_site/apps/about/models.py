from django.db import models
from markupfield.fields import MarkupField

# Create your models here.
class AboutSection(models.Model):
	title = models.CharField(max_length=200)
	body = MarkupField()


class Person(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	bio = models.TextField()
	last_updated = models.DateTimeField(auto_now_add=True)


class TeamMember(Person):
	picture = models.ImageField(upload_to="team_pics")


class BoardMember(Person):
	picture = models.ImageField(upload_to="board_pics")