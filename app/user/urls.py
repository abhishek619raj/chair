from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# from rest_framework.response import Response
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^user/$', views.UserCreate.as_view(), name='account-create'),
    # url(r'^authenticate/', CustomObtainAuthToken.as_view())
]

