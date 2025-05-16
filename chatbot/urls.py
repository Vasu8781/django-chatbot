from django.urls import path
from .views import ChatAPIView, index

urlpatterns = [
    path('', index, name='chat_home'),  # frontend page
    path('chat/', ChatAPIView.as_view(), name='chat_api'),  # chat API endpoint
]
from django.urls import path
from .views import ChatAPIView, index  # make sure 'index' is imported
