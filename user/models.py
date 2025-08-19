from django.db import models

# Create your models here.
class addcart(models.Model):
    farmer_name=models.CharField(max_length=20,default='')
    total=models.CharField(max_length=20,default='')
    created_at=models.CharField(max_length=50,default='')
    status=models.CharField(max_length=20,default='New')
    product_name=models.CharField(max_length=20,default='')
    quantity=models.CharField(default='',max_length=20)
    price_per_kg=models.CharField(max_length=20,default=0)
    note=models.CharField(max_length=1200,default='Note')
    customer_name=models.CharField(max_length=20,default='')
    phone=models.CharField(max_length=10,default=0)
    image_1=models.ImageField(upload_to='cart/')
    fromm=models.CharField(max_length=1200,default='')
    destination=models.CharField(max_length=220,default='')
    acceptcartid=models.CharField(max_length=20,default='')
    acceptedcartid=models.CharField(max_length=20,default='')
    