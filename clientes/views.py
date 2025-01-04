# from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Consulta
from .serializers import ConsultaSerializer
# Create your views here.

class ConsultaAPIView(ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    