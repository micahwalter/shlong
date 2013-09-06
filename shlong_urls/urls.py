from django.conf.urls import patterns, url

from shlong_urls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^shorten/$', views.shorten, name='shorten'),
	
	# all other urls
	url(r'^(?P<short_url>\w+)/$', views.get_long_url, name='redirect')
)