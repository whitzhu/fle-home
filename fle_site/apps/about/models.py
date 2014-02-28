from django.db import models
from markupfield.fields import MarkupField

class Person(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	bio = models.TextField()
	last_updated = models.DateTimeField(auto_now_add=True)


class TeamMember(Person):
	picture = models.ImageField(upload_to="team_pics")


class BoardMember(Person):
	picture = models.ImageField(upload_to="board_pics")


class PressArticle(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(max_length=200)
	publish_date = models.DateField(auto_now_add=False, auto_now=False)
	description = MarkupField()