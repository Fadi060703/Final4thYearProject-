from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from ...models import Order

class ListTotalFund(APIView):
    def get(self, request : Request ) :
        orders = Order.objects.all() 
        total_fund = getTotalFund( orders ) 
        data = { "totalSales" : str(total_fund) + ' SP' } 
        return Response( data = data , status = status.HTTP_200_OK ) 
    
    
def getTotalFund( orders )  :
    total = 0 
    for item in orders :
        total += int( item.total_fund ) 
    return total 