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
    list_display = ('rule', 'timestamp', 'ip_address', 'referrer')
    list_filter = ('referer', 'timestamp', 'rule')

    def ip_address(self, obj):
        return "<a href='https://freegeoip.net/json/%s' target='_blank'>%s</a>" % (obj.ip, obj.ip)
    ip_address.admin_order_field = "ip"
    ip_address.allow_tags = True
    ip_address.short_description = "IP Address"

    def referrer(self, obj):
        if obj.referer:
            return "<a href='%s' target='_blank'>%s</a>" % (obj.referer, obj.referer)
        else:
            return ""
    referrer.admin_order_field = "referer"
    referrer.allow_tags = True

admin.site.register(RedirectLogEntry, RedirectLogEntryAdmin)
