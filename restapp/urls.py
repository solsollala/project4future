from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sa_webhook$', views.sa_webhook, name='sa_webhook'),
]