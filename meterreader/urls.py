from django.urls import  path
from meterreader import views
urlpatterns = [
    path('',views.meterreader,name='meterreaderhome'),
    
]