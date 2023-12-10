# checklist/urls.py
from django.urls import path
from .views import checklist, update_grade

urlpatterns = [
    path('', checklist, name='checklist'),
    path('update/<int:enrollment_id>/', update_grade, name='update_grade'),
]
