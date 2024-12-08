from django.urls import path 
from clientes.views import index

urlpatterns= [
    path('cadastros/', index, name="cadastros")
]