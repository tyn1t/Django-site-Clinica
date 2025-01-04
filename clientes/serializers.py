from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = "__all__"