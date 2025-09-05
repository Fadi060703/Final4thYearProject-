from rest_framework import serializers 
from .models import *
from rest_framework import serializers 
from .models import *
from json.product.ProductSerializer import ProductSerializer 
class RoleSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Role 
        fields = [ 'name' ] 
class OrderProductSerializer( serializers.ModelSerializer ) :
    ProductSerializer() 
    class Meta :
        model = OrderProduct 
        fields = [ 'product' , 'quantity' ]

class OrderSerializer( serializers.ModelSerializer ) :
    order_products = OrderProductSerializer( many = True ) 
    class Meta : 
        model = Order 
        fields = [ 'order_serial_number' , 'client' , 'created_at' , 'updated_at' , 'total_fund' ] 

    def create( self , validated_data ) :
        order_products_data = validated_data.pop( 'order_products' , [] ) 
        order = Order.objects.create( **validated_data ) 
        for op in order_products_data :
            OrderProduct.objects.create( order = order , **op )
        return order 

    def update( self , instance , validated_data ) :
        order_products_data = validated_data.pop( 'order_products' , None ) 
        instance.client = validated_data.pop( 'client' , instance.client ) 
        if order_products_data is not None :
            for op in order_products_data :
                OrderProduct.objects.create( order = instance , **op )
        return instance
    





