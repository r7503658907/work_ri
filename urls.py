from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register_user'), #API
    path('api/login/',obtain_auth_token,name='login'), #API
    path('', home, name='home'),    #Animated_Home_Page


    path('home/', default, name='default'),     #E-commerce Home page
    path('login/', signup, name='login'),     #Signup button action - register.html
    path('home2/', prelogin, name='prelogin'),     #Login button action - register.html
    path('register/', register, name='register'),   #Signup button load
    path('logout/', logout_view, name='logout'),
    path('<user_id>/', user_view, name='profile'),
]
