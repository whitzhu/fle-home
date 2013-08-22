from django.conf.urls import patterns, include, url
from django.contrib import admin

from fle_redesign.apps.radpress import urls as radpress_urls

admin.autodiscover()

urlpatterns = patterns('fle_redesign.apps.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^map/$', 'map', name='map'),   
)

urlpatterns += patterns('',
	url(r'^blog/', include(radpress_urls)),
    url(r'^admin/', include(admin.site.urls)),
)