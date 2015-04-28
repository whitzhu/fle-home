import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

def get_request_ip(request):
    """Return the IP address from a HTTP request object."""
    return request.META.get("HTTP_X_FORWARDED_FOR") \
        or request.META.get("REMOTE_ADDR") \
        or request.META.get("HTTP_X_REAL_IP")  # set by some proxies


class RedirectRule(models.Model):
    slug = models.SlugField(max_length=100)
    url = models.URLField()
    login_required = models.BooleanField(help_text="Only allow logged-in users to follow this redirect", default=False)
    enabled = models.BooleanField(help_text="Enable this redirect", default=True)
    override = models.BooleanField(help_text="Override other rules with the same slug", default=False)
    notes = models.TextField(blank=True)

    def clean(self):
        # If this one is enabled, check for conflicting rules (same slug, also enabled)
        if self.enabled:
            others = RedirectRule.objects.filter(slug=self.slug, enabled=True).exclude(id=self.id)
            if others.count() > 0:
                if self.override:
                    self.override = False
                    for other in others:
                        other.enabled = False
                        other.override = False
                        other.save()
                else:
                    raise ValidationError("Other rules with the same slug are enabled. Select the override option to disable them, or use a different slug.")

    def __unicode__(self):
        return u"[%s] %s -> %s" % ("x" if self.enabled else " ", self.slug, self.url)


class RedirectLogEntry(models.Model):
    rule = models.ForeignKey(RedirectRule)
    timestamp = models.DateTimeField()
    ip = models.CharField(max_length=50, blank=True)
    referer = models.TextField(blank=True)
    user_agent = models.TextField(blank=True)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Redirect log entries"

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(RedirectLogEntry, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.datetime.now()
        request = getattr(self, "request", None)
        if request:
            self.ip = get_request_ip(request) or ""
            self.referer = request.META.get('HTTP_REFERER') or ""
            self.user_agent = request.META.get('HTTP_USER_AGENT') or ""
            if request.user.is_authenticated():
                self.user = request.user
        super(RedirectLogEntry, self).save(*args, **kwargs)