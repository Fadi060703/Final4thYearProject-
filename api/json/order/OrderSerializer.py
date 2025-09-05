from rest_framework import serializers 
from .OrderProductSerializer import OrderProductSerializer 
from ...models import Order , OrderProduct

class OrderSerializer( serializers.ModelSerializer ) :
    items = OrderProductSerializer( many = True , write_only = True )
    class Meta :
        model = Order 
        fields = [ 'client' , 'items' ] 
        
    def create( self , validated_data ) :
        items = validated_data.pop( 'items' ) 
        order_instance = Order.objects.create( **validated_data ) 
          
        for item in items :
            OrderProduct.objects.create( order = order_instance , **item )
        order_instance.save()
        return order_instance 