from cProfile import Profile
from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from .mixins import MessageHandler
from .models import *
from django.contrib.auth.forms import UserCreationForm 

import pyotp

def index(request):
    form = UserCreationForm()
    return render(request,'web/index.html',{'form':form})

def login(request):

    return render(request,'web/login.html')

def registration(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psd']
        phone = request.POST['phone']
        secret = pyotp.random_base32()
        user = User.objects.create(email = email, password = password,phone = phone)
        profile = Prfile.objects.create(user =user,auth_token = secret)
        print(profile.test_id)
        return redirect(f"/otp/{profile.test_id}")
    return render(request,"web/registration.html")

def otp(request,id):
    
    profile = Prfile.objects.get(test_id = id)
    
    totp = pyotp.TOTP(profile.auth_token)
    otp = totp.now()
    print("otp",otp) 

    if request.method == 'POST':
        enter_otp=request.POST['otp']
        print("enter otp",enter_otp)
        verification = totp.verify(enter_otp)

        if verification == True:
            return redirect("web:index")
        else :
            print("failed")
    message_handler=MessageHandler(profile.user.phone, otp).send_otp_on_phone()
    return render(request,'web/otp.html')



