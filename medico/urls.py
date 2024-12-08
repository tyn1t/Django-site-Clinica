from django.urls import path 
from medico.views import index


urlpatterns = [
    path('cadastror/', index, name="cadastror_medico")
]