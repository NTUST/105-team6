from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from team6.views import here

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'team6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
