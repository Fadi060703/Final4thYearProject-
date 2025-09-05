from rest_framework import generics , status 
from rest_framework.request import Request 
from rest_framework.response import Response
from api.json.authentication.Register import UserRegistrationSerializer
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request : Request , *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            serializer.save() 
            return Response( data = serializer.data , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 