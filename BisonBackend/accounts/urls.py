from django.urls import path
from .views import login_view, logout_view, account_view

app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('account/', account_view, name='account'),
    path('dashboard/', account_view, name='dashboard'),
    # Add other URL patterns as needed
]
