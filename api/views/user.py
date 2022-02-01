from rest_framework.views import APIView
from api.serializers.user import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        # serializer.is_valid(raise_exception= True)
        return Response({
            'data': 'Usuario logeado correctamente',
            'Token': serializer.data['token']
        }, status = status.HTTP_200_OK)

    