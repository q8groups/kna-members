from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
        url(r'^$', 'members.views.home', name='home'),
        url(r'^m/$', 'members.views.home2', name='home'),

        url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),

)
