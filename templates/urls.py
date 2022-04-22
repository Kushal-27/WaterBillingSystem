from unicodedata import name
from django.urls import path
from admin import views
urlpatterns = [
    #path('', views.adminhome, name='adminhome'),
    #path('counter/registercounter', views.registercounter, name='registercounter'),
    path('registermeter', views.registerWorkers, name='registermeter'),
    path('displaycounter', views.displayWorker, name='displaycounter'),
    path('registerworkers/<str:position>', views.registerWorkers,name='registerworkers'),
    path('displayworker/<str:position>', views.displayWorker,name='displayworker'),
    path('editworker', views.displayWorker,name='editworker'),
    path('updateworker', views.displayWorker,name='updateworker'),
    path('counter',views.counter,name='counter'),
    path('reader',views.reader,name='reader'),
    path('customer',views.customer,name='customer'),
    path('admain',views.admain,name='admain'),
    path('deleteusers/<str:email>',views.deleteusers,name='deleteusers'),
    path('addmeterreader',views.addmeterreader,name='addmeterreader'),
    path('displaymeterreader',views.displaymeterreader,name='displaymeterreader'),
    path('addcounter',views.addcounter,name='addcounter'),
    path('displaycountertable',views.displaycountertable, name='displaycountertable'),
    path('displayWorkerdata/updateWorkerdata/<str:email>',views.updateWorkerdata,name='updateWorkerdata'),
    path('displayWorkerdata/<str:email>', views.displayWorkerdata,name='displayWorkerdata'),
]