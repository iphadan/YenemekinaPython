from django.shortcuts import render
from django.http import HttpResponse
from .models import DealerProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def dealerRegister(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        firstName=request.POST.get('fname')
        lastName =request.POST.get('lname')
        email =request.POST.get('email')
        password=request.POST['password']
        repassword=request.POST.get('repassword')
        photo=request.FILES.get('photo')
        print(password)
        if repassword==password:
            try:
                user=User.objects.create(username=username,first_name=firstName,last_name=lastName,email=email,password=make_password(password))
                profile=DealerProfile.objects.create(user=user,photo=photo)
                return HttpResponse('working fine')
            #after user and profile is created ,the request should be directed to login page with success message 

            except Exception as e:
                messages.add_message(request,messages.ERROR,'error ocurred while we are processsing the data ')
                return HttpResponse('error occured')
                #error message should be shown on register page 
                

            
        else:
                messages.add_message(request,messages.ERROR,'password does not matchs')
                return HttpResponse('password does not match')
                #the request should redirected to regiser page with context values of the above fields 


       
    else:
        return render(request,'dealer/dealerregister.html')
def carPost(request):
    pass
def dealerEdit(request):
    pass
def carEdit(request):
    pass
def carDelete(request):
    pass
def dashboard(request):
    return HttpResponse('we did it')