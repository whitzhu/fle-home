from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', TemplateView.as_view(template_name='ka_lite/ka-lite.html'), name='ka_lite'),
    url(r'^faq/$', 'faq', name="faq"),
    url(r'^map/$', 'map', name="map"),
    url(r'^user-guides/$', 'user_guides', name='user_guides'),
    url(r'^user-guides/(?P<slug>.+)$', 'user_guide_detail', name='user_guide_detail'),
)
