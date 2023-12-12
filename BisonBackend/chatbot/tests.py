from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ChatSession, Message
from django.contrib.auth import get_user_model


class ChatbotAPITestCase(TestCase):
    def setUp(self):
        # Set up test user and chat session
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='12345')
        self.chat_session = ChatSession.objects.create(user=self.test_user)
        self.url = reverse('chatbot_api')  # Ensure this URL name is correctly set in urls.py

    def test_chatbot_api_response(self):
        # Simulate logging in the test user
        self.client.login(username='testuser', password='12345')

        # Test posting a message to the chatbot
        test_message = 'Hello, chatbot!'
        response = self.client.post(self.url, {'message': test_message})

        self.assertEqual(response.status_code, 201)
        # Check if the response contains the expected fields (adjust as per your API response)
        response_data = response.json()
        self.assertIn('text', response_data)
        self.assertIn('is_user_message', response_data)
        self.assertEqual(response_data['text'], test_message)
        self.assertTrue(response_data['is_user_message'])

        # Check if the message was correctly saved in the database
        self.assertTrue(Message.objects.filter(text=test_message, session=self.chat_session).exists())
