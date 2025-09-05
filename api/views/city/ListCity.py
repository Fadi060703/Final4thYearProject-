from rest_framework import status
from rest_framework.views import APIView  
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination 
from ...models import City 
from api.json.city.CitySerializer import CitySerializer 


class ListCreateCity(APIView):
    serializer_class = CitySerializer 
    
    def get(self, request : Request ):
        page = request.query_params.get( 'page' , None )
        nameFilter = request.query_params.get( 'name' , None )  
        Cities = City.objects.all()
        if nameFilter :
            Cities = City.objects.filter( name__icontains = nameFilter ) 
        serializer = self.serializer_class( Cities , many = True )
        if page is not None :
            count = Cities.count()
            paginator = PageNumberPagination()
            paginator.page_size = 5 
            paginated_res = paginator.paginate_queryset( Cities , request )
            serializer = self.serializer_class( paginated_res , many = True ) 
            return Response( data = { 'count' : count, 'data' : serializer.data }, status = status.HTTP_200_OK )
        return Response( data = { 'data' : serializer.data }, status = status.HTTP_200_OK )

    def post(self, request):
        serializer = CitySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE) 