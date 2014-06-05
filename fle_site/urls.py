from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView

import fle_site.apps.about.urls
import fle_site.apps.articles.urls
import fle_site.apps.main.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('ka_lite')), name="home"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^about/', include(fle_site.apps.about.urls)),
    url(r'^internships/', lambda request: HttpResponseRedirect(reverse('internships'))),
)

urlpatterns += patterns('fle_site.apps.ka_lite.views',
    url(r'^ka-lite/$', TemplateView.as_view(template_name='ka_lite/ka-lite.html'), name='ka_lite'),
    url(r'^ka-lite/faq/$', 'faq', name="faq")
)

urlpatterns += patterns('',
    url(r'^blog/', include(fle_site.apps.articles.urls)),
)

urlpatterns += patterns('',
    url(r'^', include(fle_site.apps.main.urls)),
)


# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

if settings.DEBUG:
    print "DEBUG is True"
    urlpatterns += patterns('',
        (r'^500/$', 'fle_site.apps.main.views.handler_500'),
        (r'^404/$', TemplateView.as_view(template_name='main/404.html')),
    )
else: 
    handler500 = 'fle_site.apps.main.views.handler_500'
    handler404 = TemplateView.as_view(template_name='main/404.html')