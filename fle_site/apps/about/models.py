from urlparse import urlparse

from markupfield.fields import MarkupField

from django.db import models
from django.template.defaultfilters import slugify

class Person(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = MarkupField(default_markup_type="html")
    last_updated = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.name)


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


class Internship(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    description = MarkupField(default_markup_type="html")
    last_updated = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.title)


class JobManager(models.Manager):
    def active(self):
        return super(JobManager, self).get_query_set().filter(active=True)


class Job(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    description = MarkupField(default_markup_type="html")
    apply_url = models.URLField()
    last_updated = models.DateTimeField(auto_now_add=True)

    objects = JobManager()

    def slug(self):
        return slugify(self.title)


class OrganizationType(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class SupportingOrganization(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    picture = picture = models.ImageField(upload_to="supporting_orgs", default=None, blank=True)
    description = MarkupField(default_markup_type="html")
    organization_type = models.ForeignKey(OrganizationType, default=None, blank=True)