from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customers,Users
#from django.db import connection


# Create your views here.


# Registers new user in the Database after fetching the data from the user
def register(request):
    if request.method == 'POST':
        cust = Customers.objects.all()
        middle_name=request.POST.get('middle_name')
        if (middle_name==NULL):
            name=  request.POST.get('first_name')+' '+ request.POST.get('last_name')
        else:
            name=  request.POST.get('first_name')+' '+middle_name+' '+ request.POST.get('last_name')    
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
        address = request.POST.get('district')+','+ request.POST.get('town')+','+ request.POST.get('municipality')+','+ request.POST.get('wardno')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            
            if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
                print('email taken')
                return redirect('register')
            else:
                saverecord = Customers(customername=name,email=email,citizenship=citizenship,address=address,password=password1)
                saverecord.save()
                print('user created')
                return render('login')
        else:
        
            return HttpResponse("Wrong password or email")
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
                    return redirect('register')
                else:
                    return redirect('register')
            return redirect('login')
        except:

            return redirect('login')


    else:

        return render(request,'login.html')


    
    