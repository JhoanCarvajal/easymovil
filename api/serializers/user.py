from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from api.models import Token


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100, write_only = True)
    token = serializers.CharField(max_length = 260, read_only = True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username = username, password = password)
        if not user:
            raise serializers.ValidationError(
                'Usuario o contraseña incorrectas'
            )
        refresh = RefreshToken.for_user(user)
        token = Token.objects.create(user = user, token = str(refresh.access_token))

        return {
            'username': str(user.username),
            'token': str(refresh.access_token)
        }
    