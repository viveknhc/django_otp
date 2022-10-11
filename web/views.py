from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from .models import *

def index(request):
    return render(request,'web/index.html')

def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if not Prfile.objects.filter(phone_number = phone_number).exists():
            return redirect('web/register')

    return render(request,'web/login.html')

def registration(request):
    if request.method == POST:
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        user = User.objects.create(username = username)
        profile = Prfile.objects.create(user = user,phone_number= phone_number)
    return redirect('web/login')



