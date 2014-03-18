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
    url(r'^about/supporters/$', 'supporters', name='supporters'),
    url(r'^about/press/$', 'press', name='press'),
    url(r'^internships/$', 'internships', name='internships'),
)

urlpatterns += patterns('fle_site.apps.ka_lite.views',
    url(r'^ka-lite/what-is-it$', 'what', name='ka_lite_what'),
    url(r'^ka-lite/how-to-install$', 'install', name='ka_lite_install'),
    url(r'^ka-lite/who-is-using-it$', 'who', name='ka_lite_who'),
    url(r'^ka-lite/can-i-contribute$', 'contribute', name='ka_lite_contribute'),
    url(r'^ka-lite/faq-and-help$', 'help', name='ka_lite_help'),   
)



urlpatterns += patterns('',
	url(r'^blog/', include(articles_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


handler500 = 'fle_site.apps.main.views.handler_500'