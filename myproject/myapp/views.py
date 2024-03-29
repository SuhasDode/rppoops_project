from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import feature

# Create your views here.
def index(request):
    features = feature.objects.all()
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already exists..')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'invalid password')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else :
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')