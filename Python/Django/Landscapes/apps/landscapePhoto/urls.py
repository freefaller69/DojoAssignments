from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<number>\d*)$', views.result),
    url(r'[^0-9]', views.index),
]
