from django.test import TestCase
from django.urls import reverse

class ReminderTests(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
