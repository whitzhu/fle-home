import settings

def debug(request):
    return {
        "base_template": "base.html",
        "debug": settings.DEBUG,
    }
