from django.conf.urls import url

from . import views

app_name = 'userProfile'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<albumId>[0-9]+)/$', views.detail, name='detail'),


    url(r'^(?P<albumId>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]