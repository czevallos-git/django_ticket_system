from django.test import TestCase
from ticketsapp.forms import TicketForm
from django.contrib.auth.models import User
from ticketsapp.models import Project

class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='john23',
            first_name='John',
            last_name='Smith',
            email= 'test@mail.com',
        )
        self.project = Project.objects.create(
            name='winep'
        )

    def test_ticket_form(self):
        form = TicketForm(data={
            'title': 'test title',
            'description': '',
            'created': '',
            'owner': self.user,
            'project': self.project
        })

        self.assertTrue(form.is_valid())

    def test_ticket_form_no_data(self):
        form = TicketForm(data={})

        self.assertFalse(form.is_valid())
        # Title and Project are mandatory fields
        self.assertEquals(len(form.errors), 2)