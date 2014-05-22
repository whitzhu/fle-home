from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

urlpatterns = patterns('fle_site.apps.ka_lite.views',
    url(r'^overview$', TemplateView.as_view(template_name='ka_lite/overview.html'), name='ka_lite_overview'),
)