# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

app_name = 'accounts'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('accounts:dashboard')  # Updated to use the app namespace
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('accounts:login')  # Updated to use the app namespace

def account_view(request):
    return render(request, 'accounts/account.html')

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
