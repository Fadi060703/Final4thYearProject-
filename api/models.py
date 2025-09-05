
from django.db import models 
from django.core.exceptions import ValidationError 
from django.utils import timezone
from django.contrib.auth.models import AbstractUser , Group , BaseUserManager,Permission
from django.utils.translation import gettext_lazy as _

''' Additionals '''
######################################################################################################################################

def validate_pos( val ) :
    if val < 0 : 
        raise ValidationError( 'Value Must Be Positive!' ) 

# Constants 

ADMIN_GROUP = 'Admin'
MANAGER_GROUP = 'Manager'
ACCOUNTANT_GROUP = 'Accountant'
SALES_GROUP = 'Sales'

class Role( models.Model ) :
    name = models.CharField( max_length = 255 ) 

    def __str__( self ) :
        return f'{ self.name }'

    class Meta :
        verbose_name ='الدور' 
        verbose_name_plural = 'الادوار'
###########################################################################################################################################
''' User Manager ''' 

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name , last_name , role , password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name = first_name , last_name = last_name , role = role , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
########################################################################################################################################### ##   #

''' Users '''
###########################################################################################################################################

class BaseUser( AbstractUser ) : # ThE Base User : 4 Different users will inherit
    class RoleChoices( models.TextChoices ) :
        MANAGER = 'manager' , _( 'Manager' ) 
        ACCOUNTANT = 'accountant', _('Accountant')
        SALESMAN = 'salesman' , _( 'Salesman' ) 
    username = None 
    email = models.EmailField( _( 'Email') , unique = True )
    first_name = models.CharField( max_length = 35 )
    last_name = models.CharField( max_length = 35 )
    role = models.CharField( choices = RoleChoices.choices , max_length = 25 , blank = True , null = True )
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [ 'first_name' , 'last_name' , 'role' ]  

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)


    objects = MyUserManager() 

    class Meta :
        verbose_name = 'المستخدم'
        verbose_name_plural = 'المستخدمون'

    def str( self ) :
        return f'{ self.email }' 

##########################################################################################################################################################

''' SIMPLE CRUD'S'''
##########################################################################################################################################################

class City( models.Model ) :
    name = models.CharField( max_length = 30, unique = True, )


    class Meta :
        verbose_name_plural = 'المدن'

    def __str__( self ) :
        return f'{ self.name }' 
    
class Lab( models.Model ) :
    name = models.CharField( max_length = 255 )  
    city = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'labLocation',blank=True ,null=True, default="homs") 

    class Meta : 
        verbose_name_plural = 'المعامل'

    def __str__( self ) : 
        return f'{ self.name } + ( { self.city } )'
   
class Product( models.Model ) :
    class Type( models.TextChoices ) :
        TABLET = 'Tablet' , 'TABLET' 
        SYRUP = 'Syrup' , 'SYRUP' 
        CREAM = 'Cream' , 'CREAM' 
        SANITIZER = 'Sanitizer' , 'SANITIZER' 
        OTHER = 'Other' , 'OTHER' 
    
    class Meta : 
        verbose_name_plural = 'المنتجات'


    name = models.CharField( max_length = 255 ) 
    manufacturing_lab = models.ForeignKey( Lab , on_delete = models.CASCADE , related_name = 'product_lab',blank=True ,null=True ) 
    type = models.CharField( choices = Type.choices , max_length = 10 ) 
    man_price = models.DecimalField( max_digits = 12 , decimal_places = 1, blank=True ,null=True) 
    sell_price = models.DecimalField( max_digits = 12 , decimal_places = 1 ,blank=True ,null=True)  
    code = models.CharField( max_length = 30 , blank = True , unique = True )
    
    def save( self , *args , **kwargs ) :
        if not self.code :
            letter = self.manufacturing_lab.name[ 0 ] 
            time_part = timezone.now().strftime( "%H%M%S" ) 
            date_part = timezone.now().strftime( "%d%m%Y" )
            self.code = f'{ letter }-{ time_part }{ date_part }' 
        super().save( *args , **kwargs )

    def __str__( self ) :  
        return f'{ self.name } + ( { self.manufacturing_lab } )'
 
##########################################################################################################################################################

''' Core Models '''
##########################################################################################################################################################


class Client( models.Model ) : # Not Finished
    name = models.CharField( max_length = 255 )
    pharmacy_name = models.CharField( max_length = 255 )  
    city = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'pharm_city' ) 
    email = models.EmailField( blank = True )
    location = models.TextField() 
    phone_number = models.CharField( max_length = 10 ) 
    pharmacy_number = models.CharField( max_length = 255 ) 

    class Meta :
        verbose_name = 'العميل'
        verbose_name_plural = 'العملاء'

    def __str__( self ) :
        return f'{ self.name } + ( { self.pharmacy_name } )' 

class ProductStock( models.Model ) :

    product = models.ForeignKey( Product , on_delete = models.CASCADE , related_name = 'tracking_stocks' ) 
    stock = models.IntegerField( default = 0 , blank = True , null = False , validators = [ validate_pos ] )

    class Meta :
        verbose_name = 'كمية منتج'
        verbose_name_plural = 'كمية المنتجات'

    def __str__( self ) :
        return f'{ self.product.name } + ( { self.stock } )' 
    

class Order( models.Model ) :
    order_serial_number = models.CharField( max_length = 255 , blank = True , null = False , unique = True )
    client = models.ForeignKey( Client , on_delete = models.CASCADE  , blank = True , null = True ) 
    created_at = models.DateTimeField( auto_now_add = True ) 
    updated_at = models.DateTimeField( auto_now_add = True ) 
    total_fund = models.DecimalField( max_digits = 15 , decimal_places = 4 ,blank=True, null=True)


    def save( self , *args , **kwargs ) :
        if not self.order_serial_number : # Code Generating
            time_part = timezone.now().strftime( "%H%M%S" ) 
            date_part = timezone.now().strftime( "%d%m%Y" )
            self.order_serial_number = f'{ time_part }{ date_part }' 
        super().save( *args , **kwargs )
        
        if hasattr(self, 'order_products'):
            total = sum(item.product.man_price * item.quantity for item in self.order_products.all())
            self.total_fund = total
            # Save again with the calculated total
            super().save(update_fields=['total_fund'])
            
    class Meta :
        verbose_name = 'طلب'
        verbose_name_plural = 'طلبات'
        
class OrderProduct( models.Model ) :
    order = models.ForeignKey( Order , on_delete = models.CASCADE , related_name = 'order_products',blank=True, null=True) 
    product = models.ForeignKey( Product , on_delete = models.CASCADE ) 
    quantity = models.IntegerField( default = 1 ) 

    class Meta : 
        unique_together = ( 'order' , 'product' ) 
        verbose_name = 'عنصر' 
        verbose_name_plural = 'عناصر'