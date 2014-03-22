from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('fle_site.apps.about.views',
    url(r'^$', direct_to_template, {'template': 'about/mission.html'}, name='mission'),
    url(r'^team/$', 'team', name='team'),
    url(r'^board/$', 'board', name='board'),
    url(r'^supporters/$', 'supporters', name='supporters'),
    url(r'^press/$', 'press', name='press'),
    url(r'^internships/$', 'internships', name='internships'),
)
