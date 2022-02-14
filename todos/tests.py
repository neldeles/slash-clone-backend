from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()
        Task.objects.create(task="today task", status="TODAY", user=testuser1)
        Task.objects.create(task="this week task", status="THIS_WEEK", user=testuser1)
        Task.objects.create(task="done task", status="DONE", user=testuser1)

    def test_task_today(self):
        task = Task.objects.filter(status="TODAY")
        expected_task = f"{task[0].task}"
        self.assertEqual(expected_task, "today task")

    def test_task_this_week(self):
        task = Task.objects.filter(status="THIS_WEEK")
        expected_task = f"{task[0].task}"
        self.assertEqual(expected_task, "this week task")

    def test_task_done(self):
        task = Task.objects.filter(status="DONE")
        expected_task = f"{task[0].task}"
        self.assertEqual(expected_task, "done task")
