from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.exceptions import NotFound 
from api.json.lab.LabSerializer import LabSerializer 
from ...models import Lab 
   
class LabDetailUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return Lab.objects.get(pk=pk)
        except Lab.DoesNotExist:
            raise NotFound(detail="Lab does not exist",code=404)
    def get(self, request, pk):
        lab = self.get_object(pk)
        serializer =LabSerializer(lab)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self, request, pk):
        lab = self.get_object(pk)
        serializer =LabSerializer(lab,data=request.data , partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        lab = self.get_object(pk)
        lab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

