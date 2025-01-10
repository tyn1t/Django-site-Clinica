from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated 

from rest_framework import status
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

import secrets

from .models import Codigo
from .serializers import (
    RegistroSerializer,
    LoginSerializer,
    UpdatePasswordSerializer,
    CodigoSerializer,
    EmailValidationSerializer
    )


class RegistroViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data) 
            return Response({'detail': 'Usuario Criado com succes.'},status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError: 
            return Response({'detail': 'Usuário com este e-mail já existe.'}, status=status.HTTP_400_BAD_REQUEST)


class LoginViews(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(username=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user=user)
            return Response(
                {
                    'refresh': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                , status=status.HTTP_200_OK)
        else:
            return Response(
                { 
                    'detail': 'Credenciais inválidas.'
                }, 
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["access_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   
        
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


class PasswordUpdateView(generics.CreateAPIView):
    
    serializer_class = UpdatePasswordSerializer
    
    def put(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if not email:
            return Response({"error": _("Email field required")}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise NotFound(detail=_("User not found."))

        serializer = UpdatePasswordSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": _("Password updated successfully.")}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Email(generics.CreateAPIView):
    serializer_class = EmailValidationSerializer
    
    def post(self, request):
        serializer = EmailValidationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            print(email)
            return Response({"detail": "Successfully email"}, status=status.HTTP_200_OK)
        return Response({"detail": "Error email"}, status=status.HTTP_400_BAD_REQUEST)