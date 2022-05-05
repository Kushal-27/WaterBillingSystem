import this
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Users
from accounts.models import Customers
from accounts.models import Rates
from counter.forms import customerforms
from django.contrib import messages
# Create your views here.
def counterhome(request):
    if request.method == "POST":
        # return HttpResponse("....")
        meternum=int(request.POST.get('meternum'))
        enteredmoney=int(request.POST.get('enteredmoney'))
       
        try:
            cust=Customers.objects.get(meternum=meternum)
            totaldue=int(cust.totaldue)
            fineamount=int(cust.fineamount)
            rates=Rates.objects.get(pk=1)
            discountrate= int(rates.discount)
            
            discountamount=0
            returnmoney=0
            if enteredmoney<totaldue:
                if fineamount==0:
                    discountamount=round((discountrate/100)*totaldue)
                    totaldue=totaldue- discountamount
                totaldue=totaldue-enteredmoney    
            else:
                totaldue=0
                returnmoney=enteredmoney-totaldue        
            thisdict={"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":cust.status,"currentunit":cust.currentunit,"discountamount": discountamount ,"fineamount":cust.fineamount,"previousunit":cust.previousunit,"totaldue":totaldue,"meternum":cust.meternum}
                
            form=customerforms(thisdict,instance=cust)
                # return HttpResponse(form)
            if form.is_valid():
                form.save()
                messages.success(request,"Meter unit added successfully")
            else:
                    # return HttpResponse("failed")
                messages.success(request,"Adding meter unit failed")
            returndict= {"customername":cust.customername,"email":cust.email,"citizenship":cust.citizenship,"address":cust.address,"password":cust.password,"status":cust.status,"currentunit":cust.currentunit,"discountamount": discountamount ,"fineamount":cust.fineamount,"previousunit":cust.previousunit,"totaldue":totaldue,"meternum":cust.meternum,"returnmoney":returnmoney}   
            return render(request,'meterreaderhome.html',thisdict)    
        except:
            return HttpResponse("User does not exist")
            messages.success(request,"Meter number does not exist")
            
            return render(request,"meterreaderhome.html")
    else:
        
        return render(request,'counterhome.html')

