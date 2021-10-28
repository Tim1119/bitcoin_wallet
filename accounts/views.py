from django.shortcuts import render,redirect
from django.views.generic import CreateView
from wallet.models import Details 
from django.contrib.auth.models import User,auth 
from django.contrib import messages
import bs4
import requests 
from bitcoin import *
# Create your views here.

def RegisterView(request):
    detail= Details()

       
    private_key = random_key() 
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    detail.private_key = private_key 
    detail.public_key = public_key 
    detail.address = address 

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        private_key = request.POST.get('private_key')
        public_key = request.POST.get('public_key')
        address = request.POST.get('address')
        print(password,password2)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Sorry, Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Sorry, Username Taken')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,last_name=private_key,first_name=address)
                user.save()
                return redirect('accounts:login')
        else:
            messages.info(request,'Password not matching')
            return redirect('accounts:register')
        return redirect('wallet:login-home')
    else:
        
        return render(request,'register.html',{'detail':detail})


def LogoutView(request):
    '''This view is responsible for logging out the user'''
    auth.logout(request)
    return redirect('wallet:welcome-home')

def LoginView(request):
    '''This view is responsible for logging in the user''' 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = auth.authenticate(username=username ,password=password) 

        if user is not None:
            auth.login(request,user)
            return redirect('wallet:logged-in-home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('accounts:login')
    else:
        return render(request,'login.html')

