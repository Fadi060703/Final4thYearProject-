from rest_framework import serializers
from ...models import City , Client 

class ClientSerializer( serializers.ModelSerializer ) :
    city = serializers.SlugRelatedField( queryset = City.objects.all() , slug_field='name' ) 
    class Meta :
        model = Client
        fields = [ 'id' , 'name' , 'pharmacy_name' , 'city' , 'location' , 'email' , 'phone_number' , 'pharmacy_number' ]

