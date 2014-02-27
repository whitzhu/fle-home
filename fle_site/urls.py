from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from fle_site.apps.articles import urls as articles_urls

admin.autodiscover()

urlpatterns = patterns('fle_site.apps.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^map/$', 'map', name='map'),
    url(r'^about/team/$', 'about_team', name='about_team'),
    url(r'^give/$', 'give', name='give'),
    url(r'^internships/$', 'internships', name='internships'),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^about/$', 'direct_to_template', {'template': 'about/about.html'}, name='about'),
    url(r'^about/board/$', 'direct_to_template', {'template': 'about/board.html'}, name='about_board'),
    url(r'^about/supporters/$', 'direct_to_template', {'template': 'about/supporters.html'}, name='about_supporters'),
)

urlpatterns += patterns('',
	url(r'^blog/', include(articles_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


handler500 = 'fle_site.apps.main.views.handler_500'