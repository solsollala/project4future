from django.conf.urls import url
from restapp import views

urlpatterns = [
    url(r'^sa$', views.sa_webhook, name='sa_webhook'),
    url(r'^dialogflow$', views.dialogflow, name='dialogflow'),
]