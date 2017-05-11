from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, nane='index'),
    url(r'^user/(?P<id>)\d+', views.show, name='show'),
]
