from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from ...models import Order 
from api.json.order.OrderSerializer import OrderSerializer 
from api.json.order.ListOrderSerializer import ListOrderSerializer 

class ListCreateOrder( APIView ) :
    def get( self , request : Request ) :
        data = Order.objects.all() 
        pharm = request.query_params.get( 'name' ) 
        city = request.query_params.get( 'city' ) 
        if pharm :
            data = data.filter( client = pharm ) 
        if city :
            data = data.filter( client__city = city )
        serializer = ListOrderSerializer( data , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    def post( self , request : Request ) :
        data = request.data 
        serializer = OrderSerializer( data = data )
        if serializer.is_valid() :
            serializer.save()
            return Response( data = serializer.data , status= status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )