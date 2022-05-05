from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Users
from accounts.models import Customers
from accounts.models import Rates
from meterreader.forms import customerforms
from django.contrib import messages
# Create your views here.
def meterreaderhome(request):
    if request.method == "POST":
        # return HttpResponse("....")
        meternum=int(request.POST.get('meternum'))
        lastestunit=int(request.POST.get('latestunit'))
       
        try:
            cust=Customers.objects.get(meternum=meternum)
            
            previousunit=int(cust.currentunit)
            
            rates=Rates.objects.get(pk=1)
            fineamount=0      
            if previousunit<lastestunit and cust.status==True:
                
                currentunit=lastestunit-previousunit
                
                if(int(cust.totaldue)!=0):              
                    fineamount=round(((int(rates.fine))/100 * (currentunit*(int(rates.rate)))))               
                    totaldue=int(cust.totaldue)+(currentunit*(int(rates.rate)))+fineamount
                else:
                    
                    totaldue=int(cust.totaldue) + currentunit*(int(rates.rate))
                # return HttpResponse(fineamount)    
                thisdict={"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":cust.status,"currentunit":lastestunit,"discountamount": 0 ,"fineamount":fineamount,"previousunit":cust.currentunit,"totaldue":totaldue,"meternum":cust.meternum}
                
                form=customerforms(thisdict,instance=cust)
                # return HttpResponse(form)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Meter unit added successfully")
                else:
                    # return HttpResponse("failed")
                    messages.success(request,"Adding meter unit failed")
            else:
                
                if previousunit > lastestunit:
                    messages.success(request,"Latest unit should be greater than previous unit")
                if cust.status== False:
                    messages.success(request,"User is inactive")
            return render(request,'meterreaderhome.html')    
        except:
            # return HttpResponse("except")
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
   