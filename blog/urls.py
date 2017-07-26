from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^map$', views.map, name='map'),
    url(r'^search$', views.search, name='search'),
    url(r'^response$', views.response, name='response')
]
