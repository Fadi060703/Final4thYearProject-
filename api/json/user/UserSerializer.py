from rest_framework import serializers 
from ...models import BaseUser 

class UserSerializer( serializers.ModelSerializer ) :

    class Meta :
        model = BaseUser 
        fields = [ 'id' ,  'email' , 'first_name' , 'last_name' , 'role' ]