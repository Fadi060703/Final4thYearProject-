from rest_framework import serializers 
from ...models import City , Lab 
class LabSerializer( serializers.ModelSerializer ) : 
    city = serializers.SlugRelatedField(queryset=City.objects.all(),slug_field='name')
    class Meta : 
        model = Lab 
        fields = [ 'id' , 'name' ,'city']
