from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from gcsdoc.rdoc.models import Doc


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Doc.objects.all(),
            context_object_name='docs',
            template_name='docs.html')),
)