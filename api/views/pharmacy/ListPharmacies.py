from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from ...models import Client 
from api.json.pharmacy.PharmacyMiniSerializer import ClientMinimalSerializer 
from api.json.pharmacy.PharmacySerializer import ClientSerializer 

class ListPharmView( APIView ) :
    serializer_class = ClientMinimalSerializer

    def get( self , request : Request ) :
        name = request.query_params.get( 'name' ) 
        city = request.query_params.get( 'city' ) 
        data = Client.objects.all()  
        if name :
            data = data.filter( name__icontains = name ) 
        if city :
            data = data.filter( city = city ) 
        serializer = self.serializer_class( data , many = True )
        data = { 'data' : serializer.data } 
        return Response( data = data , status = status.HTTP_200_OK ) 

    def post( self , request : Request ) :
        data = request.data 
        serializer = ClientSerializer( data = data ) 
        if serializer.is_valid() :
            serializer.save()
            return Response( data = serializer.data , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )