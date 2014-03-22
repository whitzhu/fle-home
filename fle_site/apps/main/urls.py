from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('fle_site.apps.main.views',
    url(r'^$', direct_to_template, {'template': 'main/home.html'}, name='home'),
    url(r'^map/$', 'map', name='map'),
    url(r'^give/$', direct_to_template, {'template': 'main/give.html'}, name='give'),
    url(r'^directions/$', direct_to_template, {'template': 'main/directions.html'}, name='directions'),
)
