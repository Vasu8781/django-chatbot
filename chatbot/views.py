from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatAPIView(APIView):
    def post(self, request):
        user_msg = request.data.get('user_message').lower()

        if "hello" in user_msg:
            bot_reply = "Hi there! How can I assist you today?"
        elif "how are you" in user_msg:
            bot_reply = "I'm doing great! Thanks for asking. How about you?"
        elif "your name" in user_msg:
            bot_reply = "I’m your friendly chatbot built with Django."
        elif "bye" in user_msg or "goodbye" in user_msg:
            bot_reply = "Goodbye! Have a great day!"
        elif "help" in user_msg:
            bot_reply = "Sure, I can help! Ask me anything about Python, Django, or life. 😉"
        else:
            bot_reply = "Sorry, I didn’t understand that. Try saying 'hello' or 'help'."

        chat = ChatMessage.objects.create(user_message=user_msg, bot_response=bot_reply)
        serializer = ChatMessageSerializer(chat)
        return Response(serializer.data)
from django.shortcuts import render

def index(request):
    return render(request, 'chatbot/index.html')
from django.shortcuts import render

def index(request):
    return render(request, 'chatbot/index.html')
