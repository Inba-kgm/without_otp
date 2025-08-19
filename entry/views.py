from django.shortcuts import render,redirect
from login.models import *
from farmer.models import *
from datetime import datetime
from django.contrib.auth import authenticate
import random
import smtplib
from email.message import EmailMessage

# Create your views here.
def login(request):
    #return render(request,'farmer/farmhome.html')
    error={"err":''}
    name=request.POST.get('name')
    pwd=request.POST.get('pass')
    user= authenticate(request,username=name,password=pwd)
    if user is not None:
         return redirect('/admin/')
    if cracc.objects.filter(username=name,password=pwd).exists():
        usr=cracc.objects.get(username=name,password=pwd)
        occp=usr.occupation
        print(occp)
        if occp=='farmer':
                request.session['mypass']=pwd
                request.session['myname']=name
                return redirect('/farmer/farmhome/')
        if occp=='buyer' or occp=='User':
                request.session['mypass']=pwd
                request.session['myname']=name
                return redirect('/user/userhome/')
        if occp=='transporter':
                request.session['mypass']=pwd
                request.session['myname']=name
                return redirect('/transporter/index/') 
        return render(request,'login/login.html',error)
    else:
        error={"err":'*Account Not Found'}
        return render(request,'login/signup.html',error)
def signup(request):
    error={"err":''}
    if request.method=="POST":
        name=request.POST.get('name')
        pwd=request.POST.get('pass')
        request.session['mypass']=pwd
        request.session['myname']=name
        cpwd=request.POST.get('cpass')
        email_id=request.POST.get('email')
        number=request.POST.get('phone')
        occp=request.POST.get('occupation')
        datee=datetime.now().date()
        usr=cracc.objects.filter(username=name,password=pwd).exists()
        if usr:
             error={"err":'*user already exists'}
             return render(request,'login/signup.html',error)
        
        usr=cracc.objects.filter(email=email_id).exists()
        if usr:
             error={"err":'*email already used'}
             return render(request,'login/signup.html',error)
        
        
        if pwd==cpwd:
            cracc.objects.create(date=datee,username=name,password=pwd,email=email_id,phone_no=number,occupation=occp)
            if occp=='farmer':
                farmmprofile.objects.create(username=name,password=pwd,email=email_id,phone=number,date=datee)
                return redirect('/farmer/farmhome/')
            if occp=='buyer':
                return redirect('/user/userproducts/')
            if occp=='transporter':
                return redirect('/transporter/index/')
        else:
            error={"err":'*Password Mismatch'}
            return render(request,'login/signup.html',error)
    return render(request,'login/login.html')
