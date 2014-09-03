import datetime
import json

from django import template
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe

register = template.Library()

def _dthandler(obj):
    "Handler for object types that are not Json-serializable"
    return  obj.isoformat() if isinstance(obj, datetime.datetime) else None


@register.filter("jsonify_obj")
def jsonify(object):
    try:
        if isinstance(object, QuerySet):
            return serialize('json', object)
    except:
        pass

    str = mark_safe(json.dumps(object, default=_dthandler))
    if str == "null":
        str = mark_safe("[%s]" % (",".join([json.dumps(o, default=_dthandler) for o in object])))
    return str

