from rest_framework import serializers 
from ...models import City , Client 
class ClientMinimalSerializer( serializers.ModelSerializer ) :
    city = serializers.SlugRelatedField( queryset = City.objects.all() , slug_field='name' ) 
    class Meta :
        model = Client
        fields = [ 'id' , 'pharmacy_name' , 'city' ] 