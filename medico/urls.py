from django.urls import path 
from medico.views import DataAPIView


urlpatterns = [
    path('creates/agendas/datas', DataAPIView.as_view(), name="data")
]