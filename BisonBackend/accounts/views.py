from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import customUser

def account_info(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/account.html', context)