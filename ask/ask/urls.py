from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'views.test'),
    url(r'^ask/.*$', 'qa.views.test'),
    # url(r'^', include('qa.urls')),
)
