from django.shortcuts import render

def account_info(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/account.html', context)
