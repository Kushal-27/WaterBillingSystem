from asyncio.windows_events import NULL
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customers,Users
from django.contrib import messages
#from django.db import connection


# Create your views here.


# Registers new user in the Database after fetching the data from the user
def register(request):
    if request.method == 'POST':
        cust = Customers.objects.all()
        name=request.POST.get('full_name')    
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        meternum=request.POST.get('meternum')
        if password1==password2:
            
            if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists() or cust.filter(meternum=meternum).exists():
                if cust.filter(email=email).exists():
                    messages.success(request,"Email Taken already.")
                if  cust.filter(citizenship=citizenship).exists():
                    messages.success(request,"Citizenship Taken already.")
                if cust.filter(meternum=meternum).exists():
                    messages.success(request,"Meter number registered already.")
                return render(request,'signup.html')

            else:
                saverecord = Customers(customername=name,email=email,citizenship=citizenship,address=address,password=password1,meternum=meternum)
                
                saverecord.save()
                print('user created')    
        else:
            messages.success(request,"Password & Confirm Password must be same")
        return redirect('login')
    else:
        
        return render(request,'signup.html')

# takes user email and password from user to login
def login(request):
    if request.method == 'POST':
        cust = Users.objects.all()
        email=request.POST.get('email')
        passwords = request.POST.get('password')
        try:
            # return HttpResponse(email)
            userdetail = cust.get(email=email)
            # return HttpResponse(userdetail.password)
            if passwords == userdetail.password:
                # return HttpResponse(userdetail.position)
                if(userdetail.position == "admin"):
                    return redirect('admain')
                    
                elif(userdetail.position=="Counter"):
                    return redirect('counterhome')
                elif(userdetail.position=="Customer"):
                    # return HttpResponse('error')
                    custs=Customers.objects.filter(email=email)
                    # return HttpResponse(custs)
                    return render(request,'customerhome.html',{"dat":custs})
                else:
                    return redirect('meterreaderhome')
            else:
                messages.success(request,"Wrong Password")      
            return redirect('login')
        except:
            messages.success(request,"User not found or inactive")
            return redirect('login')


    else:

        return render(request,'login.html')


    
    