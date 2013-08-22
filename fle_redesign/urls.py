from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('fle_redesign.apps.main.views',
    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)