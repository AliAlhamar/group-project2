from django.urls import path 
from noonauth import views 
from django.contrib.auth.tokens import PasswordResetTokenGenerator

urlpatterns = [
    path ('signup/',views.signup,name='signup'),
    path ('login/',views.handlelogin,name='handlelogin'),
    path ('logout',views.handleout,name='handlelogout'),
    

    ]
