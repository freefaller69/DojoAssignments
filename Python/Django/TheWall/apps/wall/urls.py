from django.conf.urls import url, include
from . import views

app_name = "wall"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^entrance$', views.entrance, name='entrance'),
    url(r'^wall$', views.wall, name='wall'),
    url(r'^post_message$', views.post_message, name='post_message'),
    url(r'^user/(?P<id>\d*)$', views.user, name='user'),
    url(r'^all_users$', views.all_users, name="all_users"),
]
