from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^question/(?P<id>\d+)/', 'qa.views.question', name='question'),
    url(r'^popular/', 'qa.views.popular', name='popular'),
    url(r'^$', 'qa.views.main', name='main'),
    url(r'^login/', 'views.test', name='login'),
    url(r'^signup/', 'views.test', name='signup'),
    url(r'^ask/', 'views.test', name='ask'),
    url(r'^new/', 'views.test', name='new'),
)
