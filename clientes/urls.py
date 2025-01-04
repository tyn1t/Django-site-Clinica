from django.urls import path 
from clientes.views import ConsultaAPIView

urlpatterns= [
    path('Consultas/', ConsultaAPIView.as_view(), name="Consulta")
]