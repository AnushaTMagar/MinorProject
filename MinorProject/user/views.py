from email import message
from multiprocessing import AuthenticationError
from click import password_option
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import NewUserForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'user/home.html',context)

def register(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()

    return render(request, 'user/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,username)
            return redirect('')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'user/login.html',context)

def logout(request):
    logout(request)
    return redirect('login')