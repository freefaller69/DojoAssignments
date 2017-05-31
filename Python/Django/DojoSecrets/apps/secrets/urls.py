from django.conf.urls import url
from . import views

app_name = "secrets"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)$', views.user, name='user'),
    url(r'^all_users/$', views.all_users, name="all_users"),
    url(r'^post_secret/$', views.post_secret, name='post_secret'),
    url(r'^secrets/$', views.secrets, name="secrets"),
    url(r'^secret_like/(?P<secret_id>\d+)$', views.secret_like, name="secret_like"),
    url(r'^delete_secret/(?P<secret_id>\d+)$', views.delete_secret, name="delete_secret"),
]
