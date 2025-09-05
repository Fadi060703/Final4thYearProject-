from rest_framework import serializers 
from api.json.lab.LabSerializer import LabSerializer 
from ...models import Product , Lab

class ProductSerializer( serializers.ModelSerializer ) :
    LabSerializer() 
    manufacturing_lab= serializers.SlugRelatedField(queryset=Lab.objects.all(),slug_field='name')
    class Meta :
        model = Product 
        fields = [ 'id' , 'name' , 'manufacturing_lab' , 'type' , 'man_price' ,
                   'sell_price' , 'code' ] 
        