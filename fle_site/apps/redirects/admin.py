from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from .models import RedirectRule, RedirectLogEntry


class RedirectRuleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'url', 'enabled', 'login_required')
    list_editable = ('enabled', 'login_required')
    list_filter = ('enabled', 'login_required')

admin.site.register(RedirectRule, RedirectRuleAdmin)


class RedirectLogEntryAdmin(admin.ModelAdmin):
    list_display = ('rule', 'timestamp', 'ip', 'referer')
    list_filter = ('referer', 'timestamp')

admin.site.register(RedirectLogEntry, RedirectLogEntryAdmin)
