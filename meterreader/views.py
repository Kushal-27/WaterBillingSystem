from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.models import Users
from accounts.models import Customers
from accounts.models import Rates
from admin.forms import userforms
from django.contrib import messages
# Create your views here.
def meterreaderhome(request):
    if request.method == 'POST':
        meternum=request.POST.get('meternum')
        lastestunit=request.POST.get('latestunit')
        try:
            cust=Customers.objects.get(meternum)
            rates=Rates.objects.get(PK=1)
            previousunit=cust.currentunit
            if previousunit < lastestunit and cust.status== True:
                currentunit=lastestunit-previousunit
                if(cust.totaldue!=0):
                    fineamount=((rates.fine)/100 * (currentunit*(rates.rate)))
                    totaldue=cust.totaldue+(currentunit*(rates.rate))+fineamount
                else:
                    totaldue=cust.totaldue + currentunit*(rates.rate)

                thisdict={"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":cust.status,"currentunit":lastestunit,"discountamount":0,"fineamount":fineamount,"previousunit":cust.currenntunit,"totaldue":totaldue,"meternum":cust.meternum}
                form=userforms(thisdict,instance=cust)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Meter unit added successfully")
                else:
                    messages.success(request,"Adding meter unit failed")
            else:
                if previousunit > lastestunit:
                    messages.success(request,"Latest unit should be greater than previous unit")
                if cust.status== False:
                    messages.success(request,"User is inactive")
                return render(request,'meterreaderhome.html')    
        except:
            messages.success(request,"Meter number does not exist")
            return render(request,"meterreaderhome.html")
    else:
        return render(request,'meterreaderhome.html')
    

def changepass(request,email):
    showall = Users.objects.get(email=email)
    return HttpResponse(showall)
    if request.method == 'post':
        pass
    else:
        return render(request,'changepass.html')
   