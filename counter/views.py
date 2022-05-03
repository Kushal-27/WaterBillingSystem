from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def counter(request):
    return render(request,'counternew.html')
