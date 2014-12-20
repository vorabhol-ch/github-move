from django.conf.urls import patterns, include, url
from django.contrib import admin
from game_center import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game_center_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^about/',views.about),
    url(r'^game/',views.game),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^add_page/(?P<category_name_slug>[\w\-]+)/$', views.add_page, name='add_page'),     # NEW MAPPING
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category')
)
#[\w] random word charactor   +same same 