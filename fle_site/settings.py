# Django settings for fle_site project.

import os

try:
    from local_settings import *
    import local_settings
except ImportError:
    local_settings = {}
                                    
def localor(setting_name, default_val):
    """Returns local_settings version if it exists (and is non-empty), otherwise uses default value"""
    return hasattr(local_settings, setting_name) and getattr(local_settings, setting_name) or default_val

DEBUG          = getattr(local_settings, "DEBUG", False)
TEMPLATE_DEBUG = getattr(local_settings, "TEMPLATE_DEBUG", DEBUG)

#retrieve Constantcontact info from local_settings
CONSTANT_CONTACT_API_KEY = getattr(local_settings, "CONSTANT_CONTACT_API_KEY", 'api-key-not-found')
CONSTANT_CONTACT_ACCESS_TOKEN = getattr(local_settings, "CONSTANT_CONTACT_ACCESS_TOKEN", 'access-token-not-found')
CONSTANT_CONTACT_API_URL = getattr(local_settings, "CONSTANT_CONTACT_API_URL", 'api-url-not-found')
CONSTANT_CONTACT_LIST_ID = getattr(local_settings, "CONSTANT_CONTACT_LIST_ID", 'list-id-not-found')

ADMINS = (
    # ('Dylan', 'dylan@learningequality.org'),
)

MANAGERS = ADMINS

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

# To render map, define GEOIPDAT and IPS_FILEPATH in local_settings.py ex:
# import os
# DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static/data/")
# GEOIPDAT = os.path.join(DATA_PATH, "GeoLiteCity.dat")
# IPS_FILEPATH = os.path.join(DATA_PATH, "ips.txt")

LOCATIONS_JSONP_URL = getattr(local_settings, "LOCATIONS_JSONP_URL", "https://kalite.learningequality.org/media/locations/locations.jsonp")

INDIEGOGO_API_DATA_LOCATION = getattr(local_settings, "INDIEGOGO_API_DATA_LOCATION", PROJECT_PATH)

INDIEGOGO_SUMMARY_URL = getattr(local_settings, "INDIEGOGO_SUMMARY_URL", "")

INDIEGOGO_CONTRIBUTORS_URL = getattr(local_settings, "INDIEGOGO_CONTRIBUTORS_URL", "")

DATABASES = localor("DATABASES", {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, '..', 'database.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
})

#GEO IP Data
GEO_IP_DOWNLOAD_URL = getattr(local_settings, "GEO_IP_DOWNLOAD_URL", "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz")
GEO_IP_DATA_PATH = getattr(local_settings, "GEO_IP_DATA_PATH", os.path.join(PROJECT_PATH, "..", "data", "GeoLiteCity.dat"))
ISO_COUNTRY_LIST_DATA_PATH = getattr(local_settings, "ISO_COUNTRY_LIST_DATA_PATH", os.path.join(PROJECT_PATH, "..", "data", "country-list-iso-codes.txt"))

INTERNAL_IPS   = getattr(local_settings, "INTERNAL_IPS", ("127.0.0.1",))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_URL      = getattr(local_settings, "MEDIA_URL", "/media/")
MEDIA_ROOT     = os.path.realpath(getattr(local_settings, "MEDIA_ROOT", os.path.join(PROJECT_PATH, "media"))) + "/"
STATIC_URL     = getattr(local_settings, "STATIC_URL", "/static/")
STATIC_ROOT    = os.path.realpath(getattr(local_settings, "STATIC_ROOT",os.path.join(PROJECT_PATH, "..", "_static_cache"))) + "/"

ALLOWED_HOSTS = ["*"]

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = getattr(local_settings, "SECRET_KEY", "@$=b3-wk2zv9oy_8dk))q_9h45pp*o=ntyh!_3bd-13p5761f%")

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fle_site.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'fle_site.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'fle_site.apps.main.custom_context_processors.debug',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django_extensions',
    'fack',
    'south',
    'file_resubmit',
    'fle_site.apps.articles',
    'fle_site.apps.main',
    'fle_site.apps.about',
    'fle_site.apps.ka_lite',
    'fle_site.apps.redirects',
    'ckeditor',
    'ckeditor_uploader',
)

CKEDITOR_UPLOAD_PATH = '/fileupload/'

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YouCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'PageBreak']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'toolbar': 'YouCustomToolbarConfig',  # put selected toolbar config here
        'tabSpaces': 4,
        'uploadUrl': CKEDITOR_UPLOAD_PATH,
        'extraPlugins': ','.join(
            [
                # you extra plugins here
                'uploadimage',
            ]),
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Django-articles settings
DISQUS_USER_API_KEY = localor("DISQUS_USER_API_KEY", "")
DISQUS_FORUM_SHORTNAME = "learningequality"


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    "file_resubmit": {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        "LOCATION": '/tmp/file_resubmit/'
    },
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

STRIPE_SECRET_API_KEY = getattr(local_settings, "STRIPE_SECRET_API_KEY", "")
STRIPE_PUBLISHABLE_API_KEY = getattr(local_settings, "STRIPE_PUBLISHABLE_API_KEY", "")
