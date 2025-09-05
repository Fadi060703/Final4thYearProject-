from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from api.json.user.UserSerializer import UserSerializer 
from api.json.authentication.Register import UserRegistrationSerializer 
from ...models import BaseUser 
class ListUsers( APIView ) :
    serializer_class = UserSerializer 

    def get( self , request : Request ) :
        data = BaseUser.objects.all() 
        serializer = self.serializer_class( data , many = True ) 
        data = { 'data' : serializer.data } 
        return Response( data = data , status = status.HTTP_200_OK )

    def post( self , request : Request ) : 
        data = request.data 
        serializer =UserRegistrationSerializer( data = data ) 
        if serializer.is_valid() :
            serializer.save()
            return Response( data = serializer.data , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
