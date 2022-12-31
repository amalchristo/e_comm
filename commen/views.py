from django.shortcuts import render

def commen(request):
    return render(request,'commen.html')

def commen_master(request):
    return render(request,'commen_master.html')

def customer_login(request):
    return render(request,'customer-login.html')

def customer_register(request):
    return render(request,'customer_register.html')

def seller_login(request):
    return render(request,'seller_login.html')

def seller_register(request):
    return render(request,'seller_register.html')


# Create your views here.
