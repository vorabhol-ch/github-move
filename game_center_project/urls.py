from django.conf.urls import patterns, include, url

from django.contrib import admin
from game_center import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game_center_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),url(r'^game_center/about/',views.about),
)
