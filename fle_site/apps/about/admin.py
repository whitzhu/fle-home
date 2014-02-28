from django.contrib import admin
from django.contrib.auth.models import User

from models import AboutSection


class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

  
admin.site.register(AboutSection, AboutSectionAdmin)

