from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('fle_site.apps.ka_lite.views',
    url(r'^what-is-it$', TemplateView.as_view(template_name='ka_lite/what-is-ka-lite.html'), name='ka_lite_what'),
    url(r'^extended-features$', TemplateView.as_view(template_name='ka_lite/extended-features.html'), name='ka_lite_extended_features'),
    url(r'^product-comparison$', TemplateView.as_view(template_name='ka_lite/product-comparison.html'), name='ka_lite_product_comparison'),
    url(r'^partner-with-us$', TemplateView.as_view(template_name='ka_lite/partner-with-us.html'), name='ka_lite_partner'),
    url(r'^join-community$', TemplateView.as_view(template_name='ka_lite/join-community.html'), name='ka_lite_community'),
    url(r'^faq-and-help$', TemplateView.as_view(template_name='ka_lite/faq-and-help.html'), name='ka_lite_help'),

    url(r'^how-to-install$', 'install', name='ka_lite_install'),
)

