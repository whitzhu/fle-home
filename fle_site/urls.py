from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView, RedirectView

import fle_site.apps.about.urls
import fle_site.apps.articles.urls
import fle_site.apps.ka_lite.urls
import fle_site.apps.main.urls
import fle_site.apps.redirects.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(fle_site.apps.main.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include(fle_site.apps.about.urls)),
    url(r'^internships/', lambda request: HttpResponseRedirect(reverse('internships'))),
    url(r'^blog/', include(fle_site.apps.articles.urls)),
    url(r'^ka-lite/', include(fle_site.apps.ka_lite.urls)),
    url(r'^r/', include(fle_site.apps.redirects.urls)),
    url(r'^homepage/', lambda request: HttpResponseRedirect(reverse('ka_lite'))),
    # url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /kolibri/", mimetype="text/plain")),
    url(r'^robots.txt$', lambda r: HttpResponse("", mimetype="text/plain")),
)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

if settings.DEBUG:
    print "DEBUG is True"
    urlpatterns += patterns('',
        (r'^404/$', 'fle_site.apps.main.views.handler_404'),
        (r'^500/$', 'fle_site.apps.main.views.handler_500'),
    )
else: 
    handler404 = 'fle_site.apps.main.views.handler_404'
    handler500 = 'fle_site.apps.main.views.handler_500'
