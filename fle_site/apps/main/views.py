import sys

from django.conf import settings
from django.http import HttpResponseServerError
from django.template.loader import render_to_string
from django.template import RequestContext

from annoying.decorators import render_to

@render_to("map.html")
def map(request): 
    return {"LOCATIONS_JSONP_URL": settings.LOCATIONS_JSONP_URL}


def handler_500(request):
    errortype, value, tb = sys.exc_info()
    context = {
        "errortype": errortype.__name__,
        "value": str(value),
    }
    return HttpResponseServerError(render_to_string("main/500.html", context, context_instance=RequestContext(request)))

