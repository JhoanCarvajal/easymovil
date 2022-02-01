from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.car import CarSerializer
from api.models import Car
from api.token import Tokens

class CarUpdateApiView(APIView, Tokens):
    def patch(self, request, pk):
        user = self.validate_token(request)
        if not user:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
        if user != "administrador":
            return Response({
                "data": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        car = Car.objects.filter(pk = pk).update(**request.data)
        return Response({
            "change": pk
        }, status = status.HTTP_200_OK)

    
    
    def delete(self, request, pk):
        user = self.validate_token(request)
        if not user:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
        if user != "administrador":
            return Response({
                "data": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        car = Car.objects.filter(pk = pk).delete()
        return Response({
            "delete": pk
        }, status = status.HTTP_200_OK)

    