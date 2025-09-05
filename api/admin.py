from django.contrib import admin
from .models import * 
# Register your models here.
admin.site.register( BaseUser ) 
admin.site.register( City ) 
admin.site.register( Lab ) 
admin.site.register( Role ) 
admin.site.register( Client  )
admin.site.register( Product ) 
admin.site.register( ProductStock ) 
admin.site.register( Order ) 
admin.site.register( OrderProduct ) 