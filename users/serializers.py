from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(Serializer):
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    error = 'Invalid email or password. Please try again'

    def validate(self, data):
        """ validate the user credentials
        """
        user = authenticate(request=self.context.get('request'), **data)

        if not user:
            raise serializers.ValidationError(self.error, code="auth")

        refresh = RefreshToken.for_user(user)

        return { 
            'refresh': str(refresh), 
            'access': str(refresh.access_token) 
        } 


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'user_id',
            'role', 
            'first_name', 
            'last_name', 
            'email', 
            'phone_number',
        )