from django.conf.urls import url
from . import views

app_name = "logreg"

urlpatterns = [
    url(r'^logout$', views.logout, name="logout"),
    url(r'^entrance/$', views.entrance, name='entrance'),
    url(r'^user_update$', views.user_update, name='user_update'),
    url(r'^user_delete$', views.user_delete, name='user_delete'),
]
