from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

# Create your views here.
def signup (request):
    
    return render(request,"authentication/signup.html"),

def handlelogin (request):
    
    return render(request,"authentication/login.html"),

def handleout (request):
    
    return redirect('/noonauth/login')
