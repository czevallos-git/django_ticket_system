from django.test import TestCase, Client
from django.urls import reverse
from ticketsapp.models import User, Ticket, Project

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login_page')
        self.register_url = reverse('register_page')

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    # def test_POST_add_new_ticket(self):
    #     Ticket.objects.create(
    #         title='test1',
    #         description='description1',
    #         project='winep',
    #         owner='test_owner'
    #     )
    #     response = self.client.post(self.create_ticket, )