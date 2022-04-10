from django.db import models

# Create your models here.
class Customers(models.Model):
    customername = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    citizenship = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

class Users(models.Model):
    email = models.EmailField(primary_key=True)
    citizenship = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

