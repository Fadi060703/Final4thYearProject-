from rest_framework import serializers 
from ...models import ProductStock 

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductStock 
        fields = [ 'product' , 'stock' ]   
         
    def create( self , validated_data ) :
        id = validated_data[ 'product' ]
        stock = validated_data[ 'stock' ]
         
        prod , created = ProductStock.objects.get_or_create( product = id , defaults= { 'stock' : stock } ) 
        if not created :
            prod.stock = prod.stock + stock 
            prod.save() 
        return prod 
        