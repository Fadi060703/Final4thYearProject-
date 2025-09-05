from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.exceptions import NotFound 
from api.json.product.ProductSerializer import ProductSerializer 
from ...models import Product 

class ProductDetailUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
           raise NotFound(detail="product does not exist",code=404)
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer =ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request, pk):
         product= self.get_object(pk)
         serializer =ProductSerializer(product,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
         product= self.get_object(pk)
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
