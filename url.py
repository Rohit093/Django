from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from WebApp.views import user

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebApp.views.home', name='home'),
    # url(r'^WebApp/', include('WebApp.foo.urls')),
     url(r'^user1/$',user),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
)
