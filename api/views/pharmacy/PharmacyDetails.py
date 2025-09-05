from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from ...models import Client 
from api.json.pharmacy.PharmacySerializer import ClientSerializer 

class PharmDetailView( APIView ) :
    serializer_class = ClientSerializer

    def get( self , request : Request , pk : int ) :
        data = Client.objects.get( pk = pk ) 
        serializer = self.serializer_class( data )
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 

    def patch( self , request : Request , pk : int ) :
        data = Client.objects.get( pk = pk ) 
        serializer = ClientSerializer(data = data , partial = True ) 
        if serializer.is_valid() :
            serializer.save()
            return Response( data = serializer.data , status = status.HTTP_200_OK ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    def delete( self , request : Request , pk : int ) :
        data = Client.objects.get( pk = pk ) 
        data.delete() 
        return Response( status = status.HTTP_200_OK ) 