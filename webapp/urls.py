from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gate, name='gate'),
    url(r'^under_construct$', views.under_construct, name='under_construct'),
    url(r'^hello/$', views.hello, name='hello'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^map$', views.map, name='map'),
    url(r'^search$', views.search, name='search'),
    url(r'^response$', views.response, name='response'),
    url(r'^preview$', views.preview, name='preview'),
    url(r'^starter_template$', views.starter_template, name='starter_template'),
    url(r'^cover$', views.cover, name='cover'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^webapp$', views.blog, name='webapp'),
    url(r'^carousel$', views.carousel, name='carousel'),
    url(r'^grid$', views.grid, name='grid'),
    url(r'^jumbotron$', views.jumbotron, name='jumbotron'),
    url(r'^jumbotron_narrow$', views.jumbotron_narrow, name='jumbotron_narrow'),
    url(r'^justified_nav$', views.justified_nav, name='justified_nav'),
    url(r'^navbar$', views.navbar, name='navbar'),
    url(r'^navbar_fixed_top$', views.navbar_fixed_top, name='navbar_fixed_top'),
    url(r'^navbar_static_top$', views.navbar_static_top, name='navbar_static_top'),
    url(r'^non_responsive$', views.non_responsive, name='non_responsive'),
    url(r'^offcanvas$', views.offcanvas, name='offcanvas'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^sticky_footer$', views.sticky_footer, name='sticky_footer'),
    url(r'^sticky_footer_navbar$', views.sticky_footer_navbar, name='sticky_footer_navbar'),
    url(r'^theme$', views.theme, name='theme'),
    url(r'^tooltip_viewport$', views.tooltip_viewport, name='tooltip_viewport'),
    url(r'^bl_dashboard$', views.bl_dashboard, name='bl_dashboard')
]

