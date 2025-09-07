from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Add custom user data to the response
        data.update({
            'user_id': self.user.id,
            'email': self.user.email,
            'role' : self.user.role ,
            'is_staff': self.user.is_staff,
            # Add any other user fields you need
        })
        return data