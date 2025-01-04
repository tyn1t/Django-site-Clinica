from rest_framework import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Data 
from .serializers import *



class DataAPIView(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer 
    permission_classes = [IsAuthenticated]



