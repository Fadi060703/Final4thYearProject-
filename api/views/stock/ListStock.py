from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from api.json.stock.StockSerializer import StockSerializerMain 
from api.json.stock.ShipmentSerializer import ShipmentSerializer
from ...models import ProductStock 
class ListProductStock(APIView):
    def get(self, request):
        product_stock = ProductStock.objects.all()
        serializer = StockSerializerMain(product_stock, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post( self , request : Request ) :
        data = request.data 
        serializer = ShipmentSerializer( data = data , many = True ) 
        if serializer.is_valid() :
            serializer.save()
            return Response( data = serializer.data , status = status.HTTP_200_OK ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
            
    