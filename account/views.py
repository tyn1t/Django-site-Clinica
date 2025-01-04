from rest_framework import status
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework.generics import  CreateAPIView
from .serializers import RegistroSerializer, LoginSerializer


class RegistroViews(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer
    # permission_classes = [IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data) 
            return Response({'detail': 'Usuario Criado com succes.'},status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError: 
            return Response({'detail': 'Usuário com este e-mail já existe.'}, status=status.HTTP_400_BAD_REQUEST)


class LoginViews(CreateAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        
        print(email, password)
        
        
        user = authenticate(username=email, password=password)
        
        
        if user:
            return Response({"detail":"succes"}, status=status.HTTP_200_OK)
        else:
            return Response(
                { 
                    'detail': 'Credenciais inválidas.'
                }, 
                status=status.HTTP_401_UNAUTHORIZED
            )

    