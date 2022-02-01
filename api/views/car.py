from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.car import CarSerializer
from api.models import Car
from api.token import Tokens

class CarApiView(APIView, Tokens):
    def post(self, request):
        user = self.validate_token(request)
        if not user:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
        if user != "administrador":
            return Response({
                "data": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = CarSerializer(data= request.data)
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.create(request.data)
        return Response({
            "create": data.pk
        }, status = status.HTTP_201_CREATED)

    
    
    def get(self, request):
        user = self.validate_token(request)
        if not user:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        car = Car.objects.all()

        serializer = CarSerializer(car, many = True)
        
        return Response({
            "data": serializer.data
        }, status = status.HTTP_200_OK)

    