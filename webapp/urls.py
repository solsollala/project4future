from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^post_list$', views.post_list, name='post_list'),
	url(r'^post_detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^map$', views.map, name='map'),
]

# DBPIA 관련
urlpatterns += [
    url(r'^search$', views.search, name='search'),
    url(r'^response$', views.response, name='response'),
    url(r'^preview$', views.preview, name='preview'),
]

# BOOTSTRAP 샘플 관련
urlpatterns += [
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
]

# 블루마린 / 다이얼로그플로우 관련
urlpatterns += [
#    url(r'^$', views.bluemarline_home, name='bluemarline_home'), # 첫화면
    url(r'^$', views.welcome_dialogflow, name='welcome_dialogflow'), # 첫화면

    url(r'^bl_dashboard$', views.bl_dashboard, name='bl_dashboard'),
    url(r'^under_construct$', views.under_construct, name='under_construct'),
    url(r'^about_us$', views.about_us, name='about_us'),
    url(r'^sna_blog$', views.sna_blog, name='sna_blog'),
]

# 로그인 관련
urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login3.html'}, name='login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^password_change/$', auth_views.password_change, {'password_change_redirect': 'password_change/done/'}),
    url(r'^password_change/done/$', auth_views.password_change_done),
]
