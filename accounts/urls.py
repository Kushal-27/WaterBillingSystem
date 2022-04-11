from django.urls import path
from accounts import views
#from admin.views import adminhome
from admin import views as sa
urlpatterns = [
    path('', views.login, name ='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('adminhome', sa.adminhome, name='adminhome')

]
