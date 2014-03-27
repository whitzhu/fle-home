from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


urlpatterns = patterns('fle_site.apps.ka_lite.views',
    url(r'^what-is-it$', TemplateView.as_view(template_name='ka_lite/about-ka-lite.html'), {"title": "What is KA Lite?"}, name='ka_lite_what'),
    url(r'^extended-features$', TemplateView.as_view(template_name='ka_lite/extended-features.html'), {"title": "Extended Features"}, name='ka_lite_extended_features'),
    url(r'^product-comparison$', TemplateView.as_view(template_name='ka_lite/product-comparison.html'), {"title": "Product Comparison"}, name='ka_lite_product_comparison'),
    url(r'^partner-with-us$', TemplateView.as_view(template_name='ka_lite/partner-with-us.html'), {"title": "Partner With Us!"}, name='ka_lite_partner'),
    url(r'^get-it$', TemplateView.as_view(template_name='ka_lite/get-ka-lite.html'), {"title": "Get KA Lite"}, name='ka_lite_get_it'),
    url(r'^join-community$', lambda request: HttpResponseRedirect("http://kalite.learningequality.org/"), name='ka_lite_community'),
    url(r'^faq-and-help$', TemplateView.as_view(template_name='ka_lite/faq-and-help.html'), {"title": "FAQ"}, name='ka_lite_help'),

    url(r'^how-to-download$', 'download_wizard', {"title": "Download Wizard"}, name='ka_lite_download'),
)

