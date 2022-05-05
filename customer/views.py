import this
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from accounts.models import Customers
 
def home(request,email):
    user = Customers.object.filter(email=email)
    return render(request,'customerhome.html',{"datas":user})