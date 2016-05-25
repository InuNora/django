from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^(?P<id>\d+)/', 'question', name='question'),
    )
