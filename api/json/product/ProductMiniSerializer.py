from rest_framework import serializers 
from ...models import Lab , Product 

class ProductMiniSerializer( serializers.ModelSerializer ) :
    manufacturing_lab = serializers.SlugRelatedField(queryset=Lab.objects.all(),slug_field='name')
    class Meta :
        model = Product 
        fields = [ 'id' , 'name' , 'manufacturing_lab' , 'type' ] 
