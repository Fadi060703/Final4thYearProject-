from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from ...models import Order 
from api.json.order.ListOrderSerializer import ListOrderSerializer 

class OrderDetailView( APIView ) :
    def get( self , request : Request , pk : int ) :
        data = Order.objects.get( pk = pk ) 
        serializer = ListOrderSerializer( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 