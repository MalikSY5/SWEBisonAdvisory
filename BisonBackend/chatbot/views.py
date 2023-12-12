from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatSession, Message
from .serializer import MessageSerializer  # You will need to create a serializer for the Message model

class ChatbotAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # This could retrieve the chat history if needed
        pass

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save(session=request.user.chat_session)
            # Here is where we call the OpenAI API or your custom logic to generate a response
            response_message = "This is a placeholder response."
            Message.objects.create(session=message.session, text=response_message, is_user_message=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

