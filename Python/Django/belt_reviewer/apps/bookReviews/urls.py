from django.conf.urls import url
from . import views

app_name = "bookReviews"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<id>\d+)$', views.book, name='book'),
    url(r'^books/$', views.books, name='books'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add_book$', views.add_book, name='add_book'),
]
