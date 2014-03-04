from urlparse import urlparse

from markupfield.fields import MarkupField

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    last_updated = models.DateTimeField(auto_now_add=True)


class TeamMember(Person):
    picture = models.ImageField(upload_to="team_pics")


class BoardMember(Person):
    picture = models.ImageField(upload_to="board_pics")


class PressLogo(models.Model):
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to="press_logos", help_text="Please only upload images 70x70!")
    def __str__(self):
        return self.title


class PressArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    publish_date = models.DateField(auto_now_add=False, auto_now=False)
    logo = models.ForeignKey(PressLogo, default=None, blank=True)

    def base_url(self):
        return urlparse(self.url).netloc
