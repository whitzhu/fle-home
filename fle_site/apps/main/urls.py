from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, RedirectView


urlpatterns = patterns(__package__ + '.views',
    url(r'^map/$', RedirectView.as_view(url=reverse_lazy('map'))),
    url(r'^give/$', TemplateView.as_view(template_name='main/give.html'), name='give'),
    url(r'^directions/$', TemplateView.as_view(template_name='main/directions.html'), name='directions'),
)
