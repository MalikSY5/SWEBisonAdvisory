# login/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import customUser
from django.contrib.auth.hashers import make_password

class LoginViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = customUser.objects.create(
            username='testuser',
            password=make_password('testpassword'),  # Use make_password to hash the password
            user_id='test123',
            email='testuser@example.com',
            role='student',
            first_name='Test',
            last_name='User'
        )

    def test_user_login_successful(self):
        client = Client()
        url = reverse('login:user_login')

        # Post valid login credentials
        response = client.post(url, {'user_id': 'test123', 'password': 'testpassword'})

        # Check that the response redirects to the student dashboard
        self.assertRedirects(response, reverse('student:dashboard'))

        # Check that the user is now logged in
        self.assertTrue(client.session['_auth_user_id'] == str(self.user.pk))

    def test_user_login_invalid_credentials(self):
        client = Client()
        url = reverse('login:user_login')

        # Post invalid login credentials
        response = client.post(url, {'user_id': 'test123', 'password': 'wrongpassword'})

        # Check that the response contains an error message
        self.assertContains(response, 'Invalid login credentials', status_code=200)

        # Check that the user is not logged in
        self.assertNotIn('_auth_user_id', client.session)

    def test_user_login_nonexistent_user(self):
        client = Client()
        url = reverse('login:user_login')

        # Post login credentials for a nonexistent user
        response = client.post(url, {'user_id': 'nonexistentuser', 'password': 'password'})

        # Check that the response contains an error message
        self.assertContains(response, 'Invalid login credentials', status_code=200)

        # Check that the user is not logged in
        self.assertNotIn('_auth_user_id', client.session)
