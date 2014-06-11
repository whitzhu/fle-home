from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', TemplateView.as_view(template_name='ka_lite/ka-lite.html'), name='ka_lite'),
    url(r'^faq/$', 'faq', name="faq"),
    url(r'^user-resources/$', 'user_resources', name='user_resources'),
    url(r'^user-resources/(?P<slug>.+)$', 'user_resource_detail', name='user_resource_detail'),
)
