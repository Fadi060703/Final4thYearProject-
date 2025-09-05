from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination 
from api.json.lab.LabSerializer import LabSerializer 
from ...models import Lab 
class ListCreateLab(APIView):
    serializer_class = LabSerializer 
    def get(self, request : Request ) :
        labs = Lab.objects.all()
        serializer = self.serializer_class( labs , many = True ) 
        page = request.query_params.get( 'page' ) 
        if page is not None :
            paginator = PageNumberPagination()
            paginator.page_size = 5 
            paginated_res = paginator.paginate_queryset( labs , request ) 
            serializer = self.serializer_class( paginated_res , many = True ) 
            data = {  'data' : serializer.data } 
            return Response( data = data , status = status.HTTP_200_OK )
        return Response( data = {  'data' : serializer.data},status=status.HTTP_200_OK)
    def post(self, request):
        serializer =LabSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)