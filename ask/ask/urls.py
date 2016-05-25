from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'qa.view.test'),
    url(r'^', include('qa.urls')),
)
