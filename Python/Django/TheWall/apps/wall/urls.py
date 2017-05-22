from django.conf.urls import url
from . import views

app_name = "wall"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^register/$', views.register, name='register'),
    url(r'^wall/\w*$', views.wall, name='wall'),
    url(r'^user/(?P<id>\d*)$', views.user, name='user'),
    url(r'^allusers/\w*$', views.all_users, name="allusers"),
]
