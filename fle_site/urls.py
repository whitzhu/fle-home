from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from fle_site.apps.radpress import urls as radpress_urls

admin.autodiscover()

urlpatterns = patterns('fle_site.apps.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^map/$', 'map', name='map'),
    url(r'^about/', 'about', name='about'),  
)

urlpatterns += patterns('',
	url(r'^blog/', include(radpress_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))


handler500 = 'fle_site.apps.main.views.handler_500'