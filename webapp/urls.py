from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.bluemarlin, name='bluemarlin'),
]


urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login3.html'}, name='login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
]
