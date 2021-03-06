from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bootstrap.views import port_services, send_email
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'admiralwww.views.home', name='home'),
    # url(r'^admiralwww/', include('admiralwww.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^port-services/', port_services, name='port_services'),
    url(r'^sendmail/$', send_email, name='sendmail'),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns