from django.conf.urls import url, include
from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_course$', views.add_course, name='add_course'),
    url(r'^destroy$', views.destroy, name='destroy'),
    url(r'^course_delete/(?P<id>\d+)$', views.course_delete, name='course_delete'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    ]
