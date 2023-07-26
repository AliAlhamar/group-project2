from django.shortcuts import render
from noonapp.models import Contact,Product,OrderUpdate,Orders
from django.contrib import messages
from math import ceil

# Create your views here.
def index (request):
    return render(request,"index.html")

def contact (request):
    return render(request,"contact.html")

def about (request):
    return render(request,"about.html")

def profile (request):
    return render(request,"about.html")

def checkout (request):
    return render(request,"about.html")

# def products (request):
#     return render(request,"products.html")

def handlerequest (request):
    return render(request,"about.html")
