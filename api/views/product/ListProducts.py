from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from api.json.product.ProductMiniSerializer import ProductMiniSerializer 
from api.json.product.ProductSerializer import ProductSerializer 
from ...models import Product 
class ListCreateProduct (APIView):
    def get(self, request : Request ):
        page = request.query_params.get( 'page' ) 
        products = Product.objects.all()
        serializer =ProductMiniSerializer(products,many = True)
        data = { 'data' : serializer.data }
        return Response(data = data,status=status.HTTP_200_OK)
    def post(self, request):
        serializer =ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)