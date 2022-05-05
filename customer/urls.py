from django.urls import  path
from customer import views
urlpatterns = [
    path('<str:email>',views.home,name='home'),
    # path('addmeter',views.addmeter,name='addmeter'),
    
]