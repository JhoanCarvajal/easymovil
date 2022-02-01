from dataclasses import field
from rest_framework import serializers
from api.models import Car, Token


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'