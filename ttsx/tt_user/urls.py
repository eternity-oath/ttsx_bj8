from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/', views.register),
    url(r'register_handle', views.register_handle),
    url(r'^register_username/$', views.register_username),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout$', views.logout),
    url(r'^index$', views.index),
    url(r'^logout/$', views.logout),
    url(r'^islogin/$', views.islogin),
    url(r'^center$', views.center),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
    url(r'^cart/$', views.cart)

]
