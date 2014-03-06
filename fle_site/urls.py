from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from fle_site.apps.articles import urls as articles_urls

admin.autodiscover()

urlpatterns = patterns('fle_site.apps.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^map/$', 'map', name='map'),
    url(r'^give/$', 'give', name='give'),
)

urlpatterns += patterns('fle_site.apps.about.views',
    url(r'^about/$', 'mission', name='mission'),
    url(r'^about/team/$', 'team', name='team'),
    url(r'^about/board/$', 'board', name='board'),
    url(r'^about/supporters/$', 'supporters', name='supporters'),
    url(r'^about/press/$', 'press', name='press'),
    url(r'^internships/$', 'internships', name='internships'),
    url(r'^ka-lite/$', 'ka_lite', name='ka_lite'),
)

urlpatterns += patterns('',
	url(r'^blog/', include(articles_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


handler500 = 'fle_site.apps.main.views.handler_500'