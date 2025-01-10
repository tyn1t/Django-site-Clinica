from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


from django.contrib.auth import get_user_model

User = get_user_model()  # Use get_user_model()
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
            return serializers.ValidationError('Informe o usename de usuário e a senha.')
        return attrs

class UpdatePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(_("Passwords do not match."))
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
        
        
class CodigoSerializer(serializers.Serializer):
    codigo = serializers.CharField()
    


class EmailValidationSerializer(serializers.Serializer):
    email = serializers.CharField()
    
    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("This email is not associated with any account.")
        return True

        