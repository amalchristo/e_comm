from django.shortcuts import render

def customer(request):
    return render(request,'customer.html')

def customer_master(request):
    return render(request,'customer_master.html')
# Create your views here.
