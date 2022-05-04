from django.urls import  path
from meterreader import views
urlpatterns = [
    path('meterreaderhome',views.meterreaderhome,name='meterreaderhome'),
    # path('addmeter',views.addmeter,name='addmeter'),
    
]