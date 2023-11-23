from django.urls import path
from .views import account_info

app_name = 'accounts'

urlpatterns = [
    path('', account_info, name='account_info'),
    # Add other URL patterns as needed
]
