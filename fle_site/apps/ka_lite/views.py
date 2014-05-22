import copy
import json
import os
import random
import pygeoip

import settings

from annoying.decorators import render_to
from fle_site.utils.utils import get_request_ip


@render_to("ka_lite/how-to-download.html")
def download_wizard(request, **kwargs):
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

    full_context = copy.copy(kwargs)
    full_context.update({
        "country_list": country_list,
        "record": record,
    })

    return full_context
