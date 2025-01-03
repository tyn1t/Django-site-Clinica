from django.urls import path 
from account.views import teste

urlpatterns= [
    path('teste/', teste, name="teste")
]