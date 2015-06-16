from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('grd.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
