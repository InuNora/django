from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^question/', include('qa.urls'), name='question'),
    url(r'^$', 'views.test', name='home'),
    url(r'^login/$', 'views.test', name='login'),
    url(r'^signup/$', 'views.test', name='signup'),
    url(r'^ask/.*$', 'views.test', name='ask'),
    url(r'^popular/$', 'views.test', name='popular'),
    url(r'^new/$', 'views.test', name='new'),
    url(r'^admin/', include(admin.site.urls)),
)
