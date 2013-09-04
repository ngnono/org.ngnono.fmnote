# -*- coding:utf-8 -*-
#!/user/bin/env python
from django.conf.urls import patterns, url
from apps.test import views

__author__ = 'ngnono'



urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'fmnote.views.home', name='home'),
                       # url(r'^fmnote/', include('fmnote.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^c/$',views.index),
                       )