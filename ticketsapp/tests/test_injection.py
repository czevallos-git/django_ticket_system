from django.test import TestCase, Client
from ticketsapp.auth import login_page
from django.urls import reverse


class TestSQLInjection(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login_page")

    def test_POST_login(self):
        response = self.client.post(
            self.login_url, data={"username": "test", "password": "entrada1"}
        )

        self.assertEquals(response.status_code, 200)
