from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Task

class TaskTests(APITestCase):

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword123",
        )

    def test_authenticated_user_can_create_task(self):
        self.client.force_authenticate(user=self.user)

        data = {
        "title": "Learn Django",
        "description": "Build a professional API",
        "completed": False,
        }

        response = self.client.post(
            "/api/tasks/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        task = Task.objects.get(title="Learn Django")

        self.assertEqual(task.owner, self.user)

    def test_unauthenticated_user_cannot_create_task(self):
        data = {
            "title": "Unauthorized task",
            "description": "This should not be created",
            "completed": False,
            }

        response = self.client.post(
            "/api/tasks/",
            data,
            format="json",
            )

        self.assertEqual(response.status_code, 401)
    def test_user_cannot_access_another_users_task(self):
        User = get_user_model()

        other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="otherpassword123",
        )

        task = Task.objects.create(
            title="Other user's task",
            description="This belongs to another user",
            owner=other_user,
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f"/api/tasks/{task.id}/"
        )

        self.assertEqual(response.status_code, 404)


    def test_user_can_update_own_task(self):
        task = Task.objects.create(
            title="Old title",
            description="Old description",
            owner=self.user,
        )

        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Updated title",
            "description": "Updated description",
            "completed": True,
        }

        response = self.client.put(
            f"/api/tasks/{task.id}/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        task.refresh_from_db()

        self.assertEqual(task.title, "Updated title")
        self.assertTrue(task.completed)

    def test_user_can_delete_own_task(self):
        task = Task.objects.create(
            title="Task to delete",
            description="This will be deleted",
            owner=self.user,
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f"/api/tasks/{task.id}/"
        )

        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Task.objects.filter(id=task.id).exists()
        )
    
    def test_user_can_complete_own_task(self):
        task = Task.objects.create(
            title="Task to complete",
            description="Complete this task",
            owner=self.user,
            completed=False,
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            f"/api/tasks/{task.id}/complete/"
        )

        self.assertEqual(response.status_code, 200)

        task.refresh_from_db()

        self.assertTrue(task.completed)