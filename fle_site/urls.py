from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

import fle_site.apps.about.urls
import fle_site.apps.articles.urls
import fle_site.apps.main.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^about/', include(fle_site.apps.about.urls)),
    url(r'^internships/', lambda request: HttpResponseRedirect(reverse('internships'))),
)

urlpatterns += patterns('fle_site.apps.ka_lite.views',
    url(r'^ka-lite$', TemplateView.as_view(template_name='ka_lite/ka-lite.html'), name='ka_lite'),
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


handler500 = 'fle_site.apps.main.views.handler_500'
#handler404 = 'fle_site.apps.main.views.handler_404'