from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def layouts_without_menu(request):
    return render(request,'layouts-without-menu.html')
# Create your views here.
