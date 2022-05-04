from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
