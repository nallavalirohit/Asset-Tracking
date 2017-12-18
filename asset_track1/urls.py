from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asset_track.views.home', name='home'),
#    url(r'^asset_track1/', include('asset_mgmt.urls')),
    url(r'^asset_track1/', include('asset_mgmt.urls')),
    url(r'^uam/', include('UAM.urls')),
    url(r'^admin/', include(admin.site.urls)),    
    url(r'^admin/jsi18n', 'django.views.i18n.javascript_catalog'),
)

