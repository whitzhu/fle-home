import sys

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404

from .models import RedirectRule, RedirectLogEntry

def redirect(request, slug):
    rule = get_object_or_404(RedirectRule, slug=slug, enabled=True)
    if rule.login_required and not request.user.is_authenticated():
        return HttpResponseNotAllowed("Please login before using this redirect.")
    logentry = RedirectLogEntry(request=request, rule=rule)
    logentry.save()
    return HttpResponseRedirect(rule.url)