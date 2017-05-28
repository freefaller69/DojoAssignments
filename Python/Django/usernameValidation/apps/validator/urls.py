from django.conf.urls import url, include
from . import views

app_name = "validator"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_username$', views.add_username, name='add_username'),
    url(r'^success$', views.success, name='success'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    ]
