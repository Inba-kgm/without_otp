from django.db import models

# Create your models here.
class cracc(models.Model):
    no_of_uploads=models.IntegerField(default=0)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    occupation=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    phone_no=models.IntegerField(default=0000000000)
    date=models.CharField(max_length=40,default='')