from asyncio.windows_events import NULL
import email
from this import d
from turtle import position
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customers
from admin.models import Users
from django.contrib import messages 
from admin.forms import userforms
from django.contrib import messages
# # Create your views here.
# Registers new employee into the database
def registerWorkers(request,position):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            if (position == 'Counter'):
                return redirect('counter')
            return redirect('registermeter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="Pass",position=position)
            saverecord.save()
            print('user created')
            return HttpResponse("Added in")
    else:
        if (position=="Counter"):
            return render(request,'counter.html')
        else:    
            return render(request,'meterreader.html')

# Returns the list of  employee details from the table that contains the given position
def displayWorker(request,position):
    showall=Users.objects.get(position=position)
    if (position == 'Counter'):
        return render(request,'counter.html',{"data":showall})
    return render(request,'meterreader.html',{"data":showall})


 # Get the matching column from the table and redirects the web page as needed   
def editWorker(request,email,position):
    
    editobj=Users.objects.get(email=email)
    if (position == 'Counter'):
        return render(request,'editcounter.html',{"Users":editobj})
    return render(request,'editmeterreader.html',{"Users":editobj})

# Gets data from the user and updates the new data in the table
def updateWorker(request,email,position):
    updateData=Users.objects.get(email=email)   
    form=userforms(request.Post,instance=updateData)
    if form.is_valid():
        form.save()
        messages.success(request,'Record successfull')
        if(position=="Counter"):
            return render(request,'Editcounter.html',{"Users":updateData})
        return render(request,'EditMeterReader.html',{"Users":updateData})
    if (position=="Counter"):
        return render(request,'Editcounter.html',"Failed" )
    return render(request,'EditMeterReader.html',"Failed" )            

#Function for deleting a user after taking the email that needs to be deleted
def Deleteusers(request,email):
    delusers=Users.objects.get(email=email) 
    delusers.delete()
    showdata=Users.objects.all()
    return render(request,"Counter.html",{"data":showdata})

#updates the status of customer into true and adds the customer into the user table
def updateCustomerStatus(request,email):
    updateData=Customers.objects.get(pk=email)
    customername=updateData.customername
    citizenship=updateData.citizenship
    address=updateData.address
    password=updateData.password
    status=True
    customertable=Customers(email=email,customername=customername,citizenship=citizenship, address=address,password=password,status=status)
    usertable=Users(email=email,citizenship=citizenship,username=customername,password=password,position="Customer")
    customertable.save()
    usertable.save() 
    return render(request,'admin.html')
    

#redirect the pages into the given html files (line 89-100)
def counter(request):
     return render(request,'counter.html')

def reader(request):
    return render(request,'meterreader.html')

def customer(request):
    return render(request,'customer.html')

def admain(request):
    return render(request,'admain.html')
