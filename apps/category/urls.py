# -*- coding:utf-8 -*-
__author__ = 'ngnono'


# -*- coding:utf-8 -*-
__author__ = 'ngnono'

from django.conf.urls import patterns, url

from apps.category.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^list/$', getlist),
                       url(r'^create/$', create),
                       url(r'^del/$', delete),
                       url(r'^update/$', update),
                       url(r'^detail/$', detail),
)