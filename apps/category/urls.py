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
                       # Examples:
                       # url(r'^$', 'fmnote.views.home', name='home'),
                       # url(r'^fmnote/', include('fmnote.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^list/$', list),
                       )