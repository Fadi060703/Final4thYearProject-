from rest_framework import serializers 
from ...models import BaseUser 

class UserSerializer( serializers.ModelSerializer ) :
    full_name = serializers.SerializerMethodField()
    class Meta :
        model = BaseUser 
        fields = [ 'id' ,  'email' , 'full_name', 'role' ]
        
    def get_full_name( self , obj ) :
        return obj.first_name + ' ' + obj.last_name 