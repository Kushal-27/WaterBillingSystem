from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.models import Users
from accounts.models import Customers
# Create your views here.
def meterreader(request):
    
    return render(request,'meterreaderhome.html')

def addmeter(request):
    if request.method == 'POST':
        meternum=request.POST.get('meternum')
        lastestunit=request.POST.get('latestunit')
        # try:
        #     cust=Customers.POST.get(meternum)
        #     if cust.previousunit < lastestunit:
        #         previousunit=cust.previousunit
        #         currentunit=cust.currentunit

def changepass(request,email):
    showall = Users.objects.get(email=email)
    return HttpResponse(showall)
    if request.method == 'post':
        pass
    else:
        return render(request,'changepass.html')