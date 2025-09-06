from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from api.json.stock.StockSerializer import StockSerializerMain 
from ...models import ProductStock 


class ListOutOfStock(APIView):
    def get(self, request : Request ):
        product_stock = ProductStock.objects.filter( stock__lt = 1000 )
        serializer = StockSerializerMain(product_stock, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)