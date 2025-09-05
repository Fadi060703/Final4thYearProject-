from rest_framework import serializers 
from ...models import BaseUser 
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , style = { 'input_type' : 'password'} )
    password_confirm = serializers.CharField( write_only = True  , style = { 'input_type' : 'password' } ) 
    class Meta:
        model = BaseUser  # Change this to the appropriate user type if needed
        fields = ['email', 'first_name' , 'last_name' , 'role' , 'password' , 'password_confirm' ]  # Add 'user_type' if you want to specify user roles

    def validate( self , data ) :
        if data[ 'password' ] != data[ 'password_confirm' ] :
            raise serializers.ValidationError( "Passwords Do Not Match" ) 
        return data 


    def create( self , validated_data ) : 
        password = validated_data.pop( 'password' ) 
        validated_data.pop( 'password_confirm' ) 
        user = BaseUser.objects.create( **validated_data )
        user.set_password( password )
        user.save()

        return user