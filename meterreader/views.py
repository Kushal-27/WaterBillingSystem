from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def meterreader(request):
    return render(request,'meterreaderhome.html')
