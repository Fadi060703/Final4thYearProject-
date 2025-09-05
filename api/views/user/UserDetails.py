from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from ...models import BaseUser 

class UserDetails( APIView ):
    
    def delete( self , request:Request , pk : int ) :
        user = BaseUser.objects.get( pk = pk ) 
        user.delete()
        return Response( status = status.HTTP_200_OK )