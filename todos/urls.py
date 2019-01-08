from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'details/(?P<id>\w{0,50})/$', views.details),
    url(r'complete/(?P<id>\w{0,50})/$', views.complete),
    url(r'add', views.add, name = 'add')
]