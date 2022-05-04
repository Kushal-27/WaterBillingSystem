from math import degrees
from django.db import models
from django.forms import NullBooleanField

# Create your models here.
class Customers(models.Model):
    customername = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    citizenship = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    meternum= models.CharField(max_length=200,unique=True,default=None)
    previousunit= models.IntegerField(default=0)
    currentunit= models.IntegerField(default=0)
    discountamount=models.IntegerField(default=0)
    fineamount=models.IntegerField(default=0)
    totaldue=models.IntegerField(default=1)

class Users(models.Model):
    email = models.EmailField(primary_key=True)
    citizenship = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Rates(models.Model):
    rate= models.IntegerField(default=0)
    fine=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)