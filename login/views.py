from django.shortcuts import render
from .models import cracc

# Create your views here.
def login_page(request):
    return render(request,'login/login.html')


def signup_page(request):
    return render(request,'login/signup.html')