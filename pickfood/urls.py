from django.conf.urls import patterns, include, url
from django.contrib import admin
from picky import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^(?P<user_id>\d+)/$', views.user, name='user'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
