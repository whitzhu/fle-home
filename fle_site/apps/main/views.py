import json
import sys
import stripe

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect, HttpResponseNotAllowed
from django.template.loader import render_to_string
from django.template import RequestContext

from annoying.decorators import render_to


class JsonResponse(HttpResponse):
    """Wrapper class for generating a HTTP response with JSON data"""
    def __init__(self, content, *args, **kwargs):
        if not isinstance(content, basestring):
            content = json.dumps(content, ensure_ascii=False)
        super(JsonResponse, self).__init__(content, content_type='application/json', *args, **kwargs)


@render_to("main/map.html")
def map(request): 
    return {"LOCATIONS_JSONP_URL": settings.LOCATIONS_JSONP_URL}


@csrf_exempt
def process_donation(request):

    if request.method != "POST":

        return HttpResponseNotAllowed("Only POST is allowed.")

    if not settings.STRIPE_SECRET_API_KEY:

        raise Exception("STRIPE_SECRET_API_KEY must be defined in settings to make payments.")

    data = json.loads(request.body)

    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here https://dashboard.stripe.com/account/apikeys
    stripe.api_key = settings.STRIPE_SECRET_API_KEY

    # Get the credit card details submitted by the form
    token = data["id"]
    amount = int(data['amount'])
    monthly = data['recurring']
    email = data['email']

    metadata = {}
    metadata.update(data)
    metadata.pop("amount", None)
    metadata.pop("email", None)
    metadata.pop("csrfmiddlewaretoken", None)
    metadata.pop("card", None)

    # Create the charge on Stripe's servers - this will charge the user's card
    try:
        if monthly:
            charge = stripe.Customer.create(
                source=token,
                quantity=amount,
                plan='le_donation_monthly_1',
                email=email,
                metadata=metadata,
            )
        else:
            charge = stripe.Charge.create(
                amount=amount, # amount in cents, again
                currency=data.get("currency") or "usd",
                source=token,
                metadata=metadata,
            )

        return JsonResponse({"status": "success", "message": "Thank you for your generous donation! We appreciate your support for our mission of promoting equal opportunities for learners around the world!"})

    except Exception, e:
        raise


def handler_500(request):
    errortype, value, tb = sys.exc_info()
    context = {
        "errortype": errortype.__name__,
        "value": str(value),
    }
    return HttpResponseServerError(render_to_string("main/500.html", context, context_instance=RequestContext(request)))

def handler_404(request):
    return HttpResponseServerError(render_to_string("main/404.html", {}, context_instance=RequestContext(request)))
