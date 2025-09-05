from django.urls import path 
from api.views.authentication.Register import UserRegistrationView 
from api.views.authentication.Login import LoginView 
from api.views.city.ListCity import ListCreateCity 
from api.views.city.CityDetail import CityDetailDelete 
from api.views.lab.ListLab import ListCreateLab 
from api.views.lab.LabDetail import LabDetailUpdateDelete 
from api.views.pharmacy.ListPharmacies import ListPharmView 
from api.views.pharmacy.PharmacyDetails import PharmDetailView 
from api.views.product.ListProducts import ListCreateProduct 
from api.views.product.ProductDetails import ProductDetailUpdateDelete 
from api.views.user.ListUsers import ListUsers 
from api.views.user.UserDetails import UserDetails 
from api.views.stock.ListStock import ListProductStock 
from api.views.order.ListOrders import ListCreateOrder 

urlpatterns = [
    path( 'register' , UserRegistrationView.as_view() , name = 'x' ) , 
    path( 'login' , LoginView.as_view() , name = 'y' ) , 
    path( 'users' , ListUsers.as_view() , name = 'users' ) , 
    path( 'users/<int:pk>' , UserDetails.as_view() , name = 'users_detail' ) ,
    path( 'cities' , ListCreateCity.as_view() , name = 'city' ) ,
    path( 'cities/<int:pk>' , CityDetailDelete.as_view() , name = 'city-d') ,
    path( 'labs' , ListCreateLab.as_view() , name = 'lab') , 
    path( 'labs/<int:pk>' , LabDetailUpdateDelete.as_view() , name = 'lab-d' ) ,
    path( 'clients' , ListPharmView.as_view() , name = 'pharm' ) ,
    path( 'clients/<int:pk>' , PharmDetailView.as_view() , name ='pharm-det' ) ,
    path( 'prods' , ListCreateProduct.as_view() , name = 'prod' ) , 
    path( 'prods/<int:pk>' , ProductDetailUpdateDelete.as_view() , name = 'prodD' ) , 
    path( 'stock' , ListProductStock.as_view() , name= 'stock-list' ) ,
    path( 'order' , ListCreateOrder.as_view() , name ='create_order' ) 
]
