from django.urls import path 
from rest_framework import routers 
from .views import RegistroViews, LoginViews


urlpatterns= [
    path('auth-users/Login/', LoginViews.as_view(), name="Login"),
    path('registros/', RegistroViews.as_view(), name="registro")
]