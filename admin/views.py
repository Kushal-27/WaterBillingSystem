from ast import Return
from asyncio.windows_events import NULL
import email
from this import d
from turtle import pos, position
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customers
from admin.models import Users
from django.contrib import messages 
from admin.forms import userforms
from django.contrib import messages
#from accounts.models import Users as sa
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
            if position=="counter":
                return redirect('counter')
            else:
                return redirect('reader')    
    else:
        if (position=="Counter"):
            return render(request,'counter.html')
        else:    
            return render(request,'meterreader.html')

# Returns the list of  employee details from the table that contains the given position
def displayWorker(request,position):
    showall=Users.objects.get(position=position)
    if (position == 'Counter'):
        return render(request,'editcountertable.html',{"data":showall})
    return render(request,'editmeterreadertable.html',{"data":showall})

def displaymeterreader(request):
    showall=Users.objects.filter(position='meterreader')
    return render(request,'editmeterreadertable.html',{"data":showall})

 # Get the matching column from the table and redirects the web page as needed   
def editWorker(request,email,position):
    
    editobj=Users.objects.get(email=email)
    if (position == 'Counter'):
        return render(request,'editcounter.html',{"Users":editobj})
    return render(request,'editmeterreader.html',{"Users":editobj})

# Gets data from the user and updates the new data in the table
def updateWorker(request,email,position):
    updateData=Users.objects.get(email=email)   
    form=userforms(request.POST,instance=updateData)
    if form.is_valid():
        form.save()
        messages.success(request,'Record successfull')
        if(position=="Counter"):
            return render(request,'editcounter.html',{"Users":updateData})
        return render(request,'editmeterreader.html',{"Users":updateData})
    if (position=="Counter"):
        return render(request,'editcounter.html',"Failed" )
    return render(request,'editmeterreader.html',"Failed" )            

#Function for deleting a user after taking the email that needs to be deleted
def deleteusers(request,email):
    try:
        delusers=Users.objects.get(email=email)
        
        position=delusers.position
        #return HttpResponse(position)
        delusers.delete()
        showall=Users.objects.all().filter(position=position)
        # return HttpResponse(showall.position)
        if position=="Customer":
            delcust=Customers.objects.get(email=email)  
            delcust.delete()
            showdata=Customers.objects.all()   
            return render(request,"admincustomer.html",{"data":showdata})
        elif position=="counter":
            
            #return HttpResponse(showall)
            #showcounter=Users.objects.all().filter(position=position)
            return render(request,"editcountertabel.html",{"data":showall})
        else:
            # return HttpResponse(showall)
            return render(request,"editmeterreadertable.html",{"data":showall})
    except:
        delcust=Customers.objects.get(email=email)
        delcust.delete()
        showdata=Customers.objects.all()   
        return render(request,"admincustomer.html",{"data":showdata})

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
     return render(request,'admincounter.html')

def reader(request):
    return render(request,'adminmeterreader.html')

def customer(request):
    showall=Customers.objects.all()
    return render(request,'admincustomer.html',{"data":showall})

def admain(request):
    return render(request,'admin.html')

def addmeterreader(request):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            
            return redirect('registermeter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="Pass",position="meterreader")
            saverecord.save()
            print('user created')
            return redirect('reader')    
    else:
        # return HttpResponse("hdsai")
        return render(request,'addmeterreader.html')

def addcounter(request):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            
            return redirect('addcounter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="Pass",position="counter")
            saverecord.save()
            print('user created')
            return redirect('counter')    
    else:
        # return HttpResponse("hdsai")
        return render(request,'addcounter.html')
    
def displaycountertable(request):
    showall=Users.objects.filter(position='Counter')
    return render(request,'editcountertabel.html',{"data":showall})

def displayWorkerdata(request,email):
    showall=Users.objects.get(email=email)
    position=showall.position
    # return HttpResponse(showall)
    if position=="Counter":
        return render(request,'editcounter.html',{"data":showall})
    return render(request,'editmeterreader.html',{"data":showall})

def updateWorkerdata(request,email):
    # return HttpResponse("dn")
    updateData=Users.objects.get(email=email)  
    # return HttpResponse(updateData) 
    form=userforms(request.POST,instance=updateData)
    position=updateData.position
    if form.is_valid():
        form.save()
        messages.success(request,'Record successfull')
        if(position=="Counter"):
            return render(request,'editcounter.html',{"data":updateData})
        return render(request,'editmeterreader.html',{"data":updateData})
    else:
        return HttpResponse("failed")