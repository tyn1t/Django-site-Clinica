from django.urls import path 
from medico.views import DataAPIView


urlpatterns = [
    path('creates/agenda/data', DataAPIView.as_view(), name="data")
]