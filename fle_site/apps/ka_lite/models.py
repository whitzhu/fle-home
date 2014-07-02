from datetime import date

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
    # Required fields
    title = models.CharField(max_length=100, help_text="Descriptive title of the project")
    slug = models.SlugField(unique=True, max_length=50, help_text="Auto-generated unique ID for the deployment.")
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=254)
    start_date = models.DateField(help_text='The date the deployment began')
    deployment_city = models.CharField(max_length=75)
    deployment_country = models.CharField(max_length=75)
    latitude = models.FloatField(help_text="In degrees, South is negative!")
    longitude = models.FloatField(help_text="In degrees, West is negative!")
    description = models.TextField()

    # optional bonus fields
    organization_name = models.CharField(max_length=150, blank=True)
    organization_url = models.URLField(blank=True)
    organization_city = models.CharField(max_length=100, blank=True)
    organization_country = models.CharField(max_length=100, blank=True)
    num_students = models.CharField(max_length=20, blank=True, verbose_name=u'Number of students', help_text='Range of the number of students')
    student_age_range = models.CharField(max_length=75, blank=True, verbose_name=u'Age range of students', help_text='Range of age of students')
    num_kalite_servers = models.IntegerField(blank=True, null=True, verbose_name=u'Number of KA Lite servers')
    server_os = models.CharField(max_length=75, blank=True, verbose_name=u'Operating System(s)', help_text='The operating system(s) being used in this deployment')
    hardware_setup = models.TextField(blank=True, help_text='Short description of the way the hardware is configured. E.g. 2 RPi running local WiFi content servers.')
    deployment_setting = models.CharField(max_length=100, blank=True, help_text='Short decription of where KA Lite is being used e.g. safe-learning space in a slum')
    pedagogical_model = models.CharField(max_length=100, blank=True)
    guest_blog_post = models.URLField(blank=True, help_text='Link to Guest Blog Post')

    # pictures!! 

    def __str__(self):
        return self.title

    def clean(self):
        """Ensure that organization city and country are supplied together or not at all"""
        cleaned_data = super(DeploymentStory, self).clean()
        if (self.organization_city or self.organization_country) and not (self.organization_city and self.organization_country):
            raise ValidationError("If you supply an organization city, you must supply the organization_country, and vice versa")
        # Enforce an org name if URL is provided (but not vice versa b/c some orgs may not have websites)
        if self.organization_url and not self.organization_name:
            raise ValidationError("You must provide an organization name if the organization has a website!")
        return cleaned_data

    def linked_org_name(self):
        """Return HTML anchored org name if URL exists, otherwise just org name"""
        if self.organization_url:
            return "<a href='%(url)s'>%(org_name)s</a>" % {'url': self.organization_url, 'org_name': self.organization_name}
        elif self.organization_name:
            return self.organization_name
        else:
            return False

    def age_of_deployment(self):
        """Return total age of deployment by subtracting current date from start date"""
        return "%d days" % (self.start_date - date.today()).days
        
    def lat_long(self):
        return "(%(latitude)f, %(longitude)f)" % {'latitude': self.latitude, 'longitude': self.longitude}

    def deployment_location(self):
        return "%(city)s, %(country)s" % {'city': self.deployment_city, 'country': self.deployment_country}

    def organization_location(self):
        if self.organization_city:
            return "%(city)s, %(country)s" % {'city': self.organization_city, 'country': self.organization_country} 
        else:
            return False