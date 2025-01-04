from django.contrib.auth.models import User
from rest_framework import serializers


class RegistroSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
        extra_kwargs  = {'password': {'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(
            username=  validated_data.get('email'),
            email=validated_data.get('email'),
            password=password,
            first_name=validated_data.get('username')
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            pass
        else:
            return serializers.ValidationError('Informe o nome de usuário e a senha.')
        return attrs
        