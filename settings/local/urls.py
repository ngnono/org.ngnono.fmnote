from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'fmnote.views.home', name='home'),
                       # url(r'^fmnote/', include('fmnote.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^bill/', include('apps.bill.urls')),
                       url(r'^account/', include('apps.account.urls')),
                       url(r'^category/', include('apps.category.urls')),
                       #url(r'^tag/', include('apps.tag.urls')),
                       url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)

