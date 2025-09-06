from rest_framework import serializers 
from ...models import Order , Client
from .OrderProductSerializer import OrderProductSerializer 

class ListOrderSerializer( serializers.ModelSerializer ) :
    client = serializers.SlugRelatedField( queryset = Client.objects.all() , slug_field = 'pharmacy_name' ) 
    order_products = OrderProductSerializer( read_only = True , many = True )
    class Meta :
        model = Order 
        fields = [ 'id' ,  'client' , 'order_serial_number' , 'created_at' , 'updated_at' , 'total_fund' , 'order_products' ]   
        