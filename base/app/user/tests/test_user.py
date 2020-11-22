from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

TOKEN_URL = reverse('user:token')


def create_user(**params):
    """Helper to create users for our tests"""

    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """Test the users API public"""

    def setUp(self):
        self.client = APIClient()

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""

        payload = {
            'email': 'test@test.com',
            'password': 'testpass'
        }

        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid creadentials are given"""

        create_user(email='test@test.com', password='testpass')
        payload = {
            'email': 'test@test.com',
            'password': 'wrong password'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user does not exists"""

        payload = {
            'email': 'test@test.com',
            'password': 'testpass'
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_fields(self):
        """Test that email and password are required"""

        res = self.client.post(TOKEN_URL, {'email': 'test@test.com',
                                           'password': ''})
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class PrivateUserApiTest(TestCase):
    """Test API request that require authentication"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email='test@test.com',
            password='testpass',
            name='name'
        )
        self.client.force_authenticate(user=self.user)
