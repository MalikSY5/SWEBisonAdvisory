# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_view(self):
        # Test login view renders
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

        # Test login with valid credentials
        response = self.client.post(reverse('accounts:login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertRedirects(response, reverse('accounts:dashboard'))

        # Test login with invalid credentials
        response = self.client.post(reverse('accounts:login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertContains(response, 'Invalid username or password.', html=False)

    def test_logout_view(self):
        # Log in the user first
        self.client.login(username='testuser', password='testpassword')

        # Test logout view redirects
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertRedirects(response, reverse('accounts:login'))

        # # Test user is logged out
        # response = self.client.get(reverse('accounts:account'))
        # self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_account_view(self):
        # Log in the user first
        self.client.login(username='testuser', password='testpassword')

        # Test account view renders
        response = self.client.get(reverse('accounts:account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/account.html')
