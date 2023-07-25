from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages

# Create your views here.
from django.shortcuts import render

# Create your views here.
def signup (request):
    def signup(request):
     if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            
            messages.warning(request,"password is incorrect")
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
       
        user.save()
        return HttpResponse ("user created ")
       

       

    
    return render(request,"signup.html"),

def handlelogin (request):
    
    return render(request,"login.html"),

def handleout (request):
    
    return redirect('/auth/login')
