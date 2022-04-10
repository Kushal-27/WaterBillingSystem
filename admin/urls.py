from django.urls import path
from admin import views
urlpatterns = [
    path('', views.adminhome, name='adminhome'),
    #path('counter/registercounter', views.registercounter, name='registercounter'),
    path('registermeter', views.registerWorkers, name='registermeter'),
    path('displaycounter', views.displayWorker, name='displaycounter'),
    path('registerworkers', views.registerWorkers,name='registerworkers'),
    path('displayworker', views.displayWorker,name='displayworker'),
    path('editworker', views.displayWorker,name='editworker'),
    path('updateworker', views.displayWorker,name='updateworker'),
    path('counter',views.displayWorker,name='counter'),
    path('reader',views.reader,name='reader'),
    path('customer',views.customer,name='customer'),
    path('admain',views.admain,name='admain'),

]
