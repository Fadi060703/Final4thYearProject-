from rest_framework_simplejwt.views import TokenObtainPairView
from api.json.authentication.Login import CustomTokenObtainPairSerializer

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer