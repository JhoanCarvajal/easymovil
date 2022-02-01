from platform import release
from urllib import response
from api.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.models import User

class Tokens:
    def validate_token(self, request):
        header = request.headers.get("Authorization", None)
        bearer = header.split(" ")[1]

        JWTt = JWTAuthentication()
        JWTt.get_validated_token(header.split(" ")[1])

        response = JWTt.authenticate(request)
        if response:
            user, token = response
            profile = User.objects.filter(username = user).values_list("profile__name", flat=True)
            print(profile[0])
            
            return profile[0]
        return None