from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password



# Register API

class RegisterAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegProfileSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            username = serializer.data['username']
            password = serializer.data['password']
            User.objects.create(username=username, password=make_password(password))
            user = User.objects.filter(username=serializer.data['username']).values()[0]
            print(user)
            #profile_create

            profile.objects.create(
                    username_id=user['id'],
                    profile_id=serializer.data['username']
            )

            return JsonResponse({
                    'status': status.HTTP_200_OK,
                    'message': 'Registration Successfully',
            })
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# #updateProfile
# class updateProfile(APIView):
#     def post(self,request):
#         try:
#             data = request.data
#             serializer = updateProfileSerializer(data = data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 mobile = serializer.data['mobile']
#                 password = serializer.data['password']
#                 first_name = serializer.data['first_name']
#                 last_name = serializer.data['last_name']
#                 business_name = serializer.data['business_name']
#                 gst = serializer.data['gst']
#
#                 profile.objects.filter(profile_id=user[0]).update(
#                     first_name=first_name,
#                     last_name =last_name,
#                     business_name =business_name,
#                     gst = gst,
#                     password=password
#                 )
def home(request, *args, **kwargs):
    context = dict()
    return render(request, "home.html", context)


def default(request, *args, **kwargs):
    context = dict()
    if request.method == 'POST':
        pass
    return render(request, "home2.html", context)


def register(request, *args, **kwargs):
    if request.method == 'POST':
        print('user new')
    context = dict()
    return render(request, "register.html", context)


def signup(request, *args, **kwargs):
    context = dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        url = "http://127.0.0.1:8000/api/register/"
        data={"username":username,"password":password}
        r = requests.post(url=url,data=data)
        status_code = r.status_code
        context[status_code] = status_code
        print(context)
    return render(request, "login.html", context)


def prelogin(request, *args, **kwargs):
    context = dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        login(request, user)
    return render(request, "home2.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


def user_view(request, *args, **kwargs):
    context = dict()
    user_id = kwargs.get("user_id")
    try:
        user = User.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if user:
        context['id'] = user.id
        context['username'] = user.username
        context['email'] = user.email
        # context['BASE_URL'] = settings.BASE_URL
        return render(request, "profile.html", context)