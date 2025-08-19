from django.urls import path,include
from .views import *

urlpatterns = [
    path('userhome/',userhome,name='userhome'),
    path('userorders/',userorders,name='userorders'),
    path('userprofile/',userprofile,name='userprofile'),
    path('userproducts/',userproducts,name='userproducts'),
    path('addcart/',addcarts,name='addcart'),
    path('addcartpage/',addtocart,name='addcart'),
    path('useraccepts/',accepts,name='useraccepts'),
    path('usershipped/',shipped,name='usershipped'),
    path('userdelivered/',delivered,name='userdelivered'),
    path('usercancelled/',cancelled,name='usercancelled'),
    path('userrecent/',recent,name='userrecent'),
    path('delver/',delacc,name='delver'),
]