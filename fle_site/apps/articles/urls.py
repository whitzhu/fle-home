from django.conf.urls.defaults import *

from fle_site.apps.articles import views

urlpatterns = patterns('',
    url(r'^$', views.blog_filter_page, name="blog"),
    url(r'^(?P<year>\d{4})/(?P<slug>.*)/$', views.display_article, name="articles_display_article"),

)
