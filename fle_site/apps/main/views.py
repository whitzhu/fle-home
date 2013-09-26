import pygeoip
import json
import re
import sys

from django.shortcuts import render_to_response
from django.http import HttpResponseServerError
from django.template.loader import render_to_string
from django.template import RequestContext

from fle_site import settings


def home(request):
	return render_to_response("home.html")

def map(request): 
	gic = pygeoip.GeoIP(settings.GEOIPDAT)
	ips = open(settings.IPS_FILEPATH).readlines()
	records = [gic.record_by_addr(item.strip()) for item in ips if item]
	locations = []
	existing_locations = set([(0, 0)])
	for record in records:
		if record:
			if (record['latitude'], record['longitude']) not in existing_locations:
				name = [record['city'], record['region_name'], record['country_name']]
				name = filter(lambda x: not re.match("^\d*$", x), name)
				name = ", ".join(name)
				locations.append({
					"latitude": record['latitude'],
					"longitude": record['longitude'],
					"name": name,
				})
				existing_locations.add((record['latitude'], record['longitude']))
	# remove duplicates and remove null coordinates
	# location_info = list(set(location_info) - set([(0, 0)]))
	return render_to_response('map.html', {"locations": json.dumps(locations)})

def handler_500(request):
    errortype, value, tb = sys.exc_info()
    context = {
        "errortype": errortype.__name__,
        "value": str(value),
    }
    return HttpResponseServerError(render_to_string("500.html", context, context_instance=RequestContext(request)))
