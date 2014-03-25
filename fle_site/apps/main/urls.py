from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns(__package__ + '.views',
    url(r'^$', TemplateView.as_view(template_name='main/home.html'), name='home'),
    url(r'^map/$', 'map', name='map'),
    url(r'^give/$', TemplateView.as_view(template_name='main/give.html'), name='give'),
    url(r'^directions/$', TemplateView.as_view(template_name='main/directions.html'), name='directions'),
)
