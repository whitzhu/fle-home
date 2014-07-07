from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', TemplateView.as_view(template_name='ka_lite/ka-lite.html'), name='ka_lite'),
    url(r'^faq/$', 'faq', name="faq"),
    url(r'^map/$', 'map', name="map"),
    url(r'^map/add/$', 'map_add', name="map_add"),
    url(r'^map/thankyou/$', TemplateView.as_view(template_name='ka_lite/map_add_thankyou.html'), name="map_add_thankyou"),
    url(r'^user-guides/$', 'user_guides', name='user_guides'),
    url(r'^user-guides/embed/(?P<slug>[^/]+)$', 'user_guide_detail_embed', name='user_guide_detail_embed'),
    url(r'^user-guides/(?P<slug>[^/]+)$', 'user_guide_detail', name='user_guide_detail'),
)
