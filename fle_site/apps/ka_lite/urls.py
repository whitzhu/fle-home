from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('fle_site.apps.ka_lite.views',
    url(r'^what-is-it$', direct_to_template, {'template': 'ka_lite/what-is-ka-lite.html'}, name='ka_lite_what'),
    url(r'^extended-features$', direct_to_template, {'template': 'ka_lite/extended-features.html'}, name='ka_lite_extended_features'),
    url(r'^product-comparison$', direct_to_template, {'template': 'ka_lite/product-comparison.html'}, name='ka_lite_product_comparison'),
    url(r'^partner-with-us$', direct_to_template, {'template': 'ka_lite/partner-with-us.html'}, name='ka_lite_partner'),
    url(r'^join-community$', direct_to_template, {'template': 'ka_lite/join-community.html'}, name='ka_lite_community'),
    url(r'^faq-and-help$', direct_to_template, {'template': 'ka_lite/faq-and-help.html'}, name='ka_lite_help'),

    url(r'^how-to-install$', 'install', name='ka_lite_install'),
)

