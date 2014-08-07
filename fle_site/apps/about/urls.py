from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('fle_site.apps.about.views',
    url(r'^$', TemplateView.as_view(template_name='about/mission.html'), name='mission'),
    url(r'^values/$', TemplateView.as_view(template_name='about/values.html'), name='values'),
    url(r'^team/$', 'team', name='team'),
    url(r'^board/$', 'board', name='board'),
    url(r'^supporters/$', 'supporters', name='supporters'),
    url(r'^press/$', 'press', name='press'),
    url(r'^jobs/$', 'jobs', name='jobs'),
    url(r'^internships/$', 'internships', name='internships'),
)
