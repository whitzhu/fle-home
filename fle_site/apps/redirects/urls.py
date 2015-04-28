from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse, reverse_lazy

urlpatterns = patterns(__package__ + '.views',
    url(r'^(?P<slug>[\w\-]+)/?$', "redirect", name='redirect'),
)
