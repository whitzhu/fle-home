import pygeoip
import json
import re

from django.shortcuts import render_to_response

from fle_site import settings


# gic = pygeoip.GeoIP(settings.GEOIPDAT)

def home(request):
	return render_to_response("home.html")

def map(request): 
	ips = open(settings.PROJECT_PATH + "/ips.txt").readlines()
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