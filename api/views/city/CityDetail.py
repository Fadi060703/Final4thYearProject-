from rest_framework import status
from rest_framework.views import APIView  
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.exceptions import NotFound
from ...models import City 
from api.json.city.CitySerializer import CitySerializer 


class CityDetailDelete (APIView):
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
           raise NotFound(detail="city does not exist",code=404)
           #raise Http404
    def get(self, request, pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch( self , request : Request , pk : int ) :
        city = City.objects.get( pk = pk ) 
        serializer = CitySerializer( city , data = request.data , partial = True ) 
        if serializer.is_valid() :
            serializer.save()
            return Response( data = serializer.data , status = status.HTTP_200_OK ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    def delete(self, request, pk):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

