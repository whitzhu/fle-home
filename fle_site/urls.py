from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

from fle_site.apps.articles import urls as articles_urls

admin.autodiscover()

urlpatterns = patterns('fle_site.apps.main.views',
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),
    url(r'^map/$', 'map', name='map'),
    url(r'^give/$', direct_to_template, {'template': 'give.html'}, name='give'),
    url(r'^directions/$', direct_to_template, {'template': 'directions.html'}, name='directions'),
)

urlpatterns += patterns('fle_site.apps.about.views',
    url(r'^about/$', direct_to_template, {'template': 'about/mission.html'}, name='mission'),
    url(r'^about/team/$', 'team', name='team'),
    url(r'^about/board/$', 'board', name='board'),
    url(r'^about/supporters/$', direct_to_template, {'template': 'about/supporters.html'}, name='supporters'),
    url(r'^about/press/$', 'press', name='press'),
    url(r'^internships/$', 'internships', name='internships'),
)

urlpatterns += patterns('',
	url(r'^blog/', include(articles_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


handler500 = 'fle_site.apps.main.views.handler_500'