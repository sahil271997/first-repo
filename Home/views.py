from django.shortcuts import render ,HttpResponse,redirect
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User

# Create your views here.
def index(request):
     print(request.user)
     if request.user.is_anonymous:
         return redirect("/login")
     return render(request,"index.html")
#    return HttpResponse("this is home page")

def about(request):
   return render(request,"about.html")
   # return HttpResponse("this is aboutus page")

def contact(request):
   if request.method == "POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       desc=request.POST.get('decs')
       contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
       contact.save()
       messages.success(request,"your message has been sent")
   return render(request,"contact.html")
   # return HttpResponse("this is home page")

def services(request):
   return render(request,"services.html")
   # return HttpResponse("this is home page")
def loginpage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else :
            return render(request,"login.html")
                
    return render(request,"login.html")
def logoutpage(request):
    return redirect("/login")