from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class UserRegistrationTests(APITestCase):

    def test_user_can_register(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123",
        }

        response = self.client.post(
            "/api/auth/register/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)

        User = get_user_model()

        self.assertTrue(
            User.objects.filter(username="testuser").exists()
        )

    def test_password_is_hashed(self):
        data = {
            "username": "testuser2",
            "email": "test2@example.com",
            "password": "testpassword123",
        }

        response = self.client.post(
            "/api/auth/register/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)

        User = get_user_model()
        user = User.objects.get(username="testuser2")

        self.assertNotEqual(
            user.password,
            "testpassword123"
        )

        self.assertTrue(
            user.check_password("testpassword123")
        )


class UserLoginTests(APITestCase):

    def setUp(self):
        User = get_user_model()

        User.objects.create_user(
            username="loginuser",
            email="login@example.com",
            password="correctpassword123",
        )

    def test_user_can_login(self):
        data = {
            "username": "loginuser",
            "password": "correctpassword123",
        }

        response = self.client.post(
            "/api/auth/login/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_user_cannot_login_with_wrong_password(self):
        data = {
            "username": "loginuser",
            "password": "wrongpassword",
        }

        response = self.client.post(
            "/api/auth/login/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 401)