from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from accounts.models import customUser

def user_login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # Custom logic to check the database for the user
        try:
            user = customUser.objects.get(username=user_id)
        except customUser.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            
            # Redirect to the appropriate dashboard based on the user's role
            if user.role == 'student':
                return redirect('student:dashboard')
            elif user.role == 'admin':
                return redirect('admin:dashboard')
            elif user.role == 'advisor':
                return redirect('advisor:dashboard')
        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login/login.html')
