import json 
import os 
import random
import pygeoip

import settings

from annoying.decorators import render_to
from fle_site.utils.utils import get_request_ip


@render_to("ka-lite/what-is-ka-lite.html")
def what(request):
	return {}

@render_to("ka-lite/how-to-install.html")
def install(request):
	try:
		geo_ip_data = pygeoip.GeoIP(settings.GEO_IP_DATA_PATH)
	except IOError:
		geo_ip_data = None
	try:
		country_list = [{"code": item.split(":")[0].decode('cp1252'), "name": item.split(":")[1].decode('cp1252')} for item in open(settings.ISO_COUNTRY_LIST_DATA_PATH,'r').readlines()]
	except IOError:
		country_list = None
	ip = get_request_ip(request) or ""
	if geo_ip_data and ip:
		record = geo_ip_data.record_by_addr(ip.strip())
	else:
		record = None
	return {
		"country_list": country_list,
		"record": record,
	}

@render_to("ka-lite/who-is-using-it.html")
def who(request):
	return {}

@render_to("ka-lite/can-i-contribute.html")
def contribute(request):
	return {}

@render_to("ka-lite/faq-and-help.html")
def help(request):
	return {}


