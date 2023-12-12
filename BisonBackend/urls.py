# checklist/urls.py
from django.urls import include, path
from .views import checklist, update_grade

urlpatterns = [
    path('', checklist, name='checklist'),
    path('update/<int:enrollment_id>/', update_grade, name='update_grade'),
    # path('chatbot/', include('chatbot.urls')),  # This includes the urls from chatbot app
]
