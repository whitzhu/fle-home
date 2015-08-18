import re
import sys

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404

from .models import RedirectRule, RedirectLogEntry, RedirectVariable

VARIABLE_REGEX = re.compile("%([A-Za-z0-9_]+)%")

def _replace_variable(matchobj):
    var_name = matchobj.group(1)
    try:
        return RedirectVariable.objects.get(name__iexact=var_name).value
    except RedirectVariable.DoesNotExist:
        return matchobj.group(0)

def redirect(request, slug):
    rule = get_object_or_404(RedirectRule, slug=slug, enabled=True)
    if rule.login_required and not request.user.is_authenticated():
        return HttpResponseNotAllowed("Please login before using this redirect.")
    url = re.sub(VARIABLE_REGEX, _replace_variable, rule.url)
    logentry = RedirectLogEntry(request=request, rule=rule, url=url)
    logentry.save()
    return HttpResponseRedirect(url)

