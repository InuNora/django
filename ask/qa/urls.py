from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # url(r'^(?P<id>\d+)/', 'question', name='question'),
    # url(r'^popular/$', 'views.popular', name='popular'),
    # url(r'^$', 'views.main', name='home'),
    
    # url(r'^login/$', 'test'),
    url(r'^signup/$', 'views.test'),
    # url(r'^ask/.*$', 'views.test''),
    url(r'^new/$', 'test'),
    )
