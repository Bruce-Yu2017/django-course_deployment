from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add_new),
    url(r'^remove/(?P<id>\d+)$', views.confirm_remove),
    url(r'^success_delete/(?P<id>\d+)$', views.remove)
]
