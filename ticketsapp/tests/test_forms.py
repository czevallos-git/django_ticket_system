import json
from django.test import TestCase
from ticketsapp.forms import TicketForm, CustomUserCreationForm
from django.contrib.auth.models import User
from ticketsapp.models import Project


SHORT_PASSWORD = "jhsor6"
PASSWORD_LOWER_BOUNDARY_VALUE = 'H4Kkh83k10'
PASSWORD_BOUNDARY_VALUE = 'fFJI8HFLa11'
PASSWORD_UPPER_BOUNDERY_VALUE = 'kFT4hdjrTp12'
LONG_PASSWORD = 'dlgJUR095ljd3KJ17'
COMMON_PASSWORD = 'password123'
NUMERIC_PASSWORD = '15936852365'

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

    def test_short_password_is_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': SHORT_PASSWORD,
            'password2': SHORT_PASSWORD,
        })
        
        # Minimum length has been defined in the settings.py file to be 11
        errors = json.loads(form.errors.as_json())
        self.assertEqual(len(SHORT_PASSWORD), 6)
        self.assertFalse(form.is_valid())
        self.assertEqual(errors['password2'][0]['code'], "password_too_short")

    def test_password_lower_boundary_value_is_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': PASSWORD_LOWER_BOUNDARY_VALUE,
            'password2': PASSWORD_LOWER_BOUNDARY_VALUE,
        })
        
        # Minimum length has been defined in the settings.py file to be 11
        errors = json.loads(form.errors.as_json())
        self.assertEqual(len(PASSWORD_LOWER_BOUNDARY_VALUE), 10)
        self.assertFalse(form.is_valid())
        self.assertEqual(errors['password2'][0]['code'], "password_too_short")

    def test_password_boundary_value_is_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': PASSWORD_BOUNDARY_VALUE,
            'password2': PASSWORD_BOUNDARY_VALUE,
        })
        
        # Minimum length has been defined in the settings.py file to be 11
        self.assertEqual(len(PASSWORD_BOUNDARY_VALUE), 11)
        self.assertTrue(form.is_valid())

    def test_password_upper_boundary_value_is_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': PASSWORD_UPPER_BOUNDERY_VALUE,
            'password2': PASSWORD_UPPER_BOUNDERY_VALUE,
        })
        
        # Minimum length has been defined in the settings.py file to be 11
        self.assertEqual(len(PASSWORD_UPPER_BOUNDERY_VALUE), 12)
        self.assertTrue(form.is_valid())
    
    def test_long_password_is_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': LONG_PASSWORD,
            'password2': LONG_PASSWORD,
        })
        
        # Minimum length has been defined in the settings.py file to be 11
        self.assertEqual(len(LONG_PASSWORD), 17)
        self.assertTrue(form.is_valid())

    def test_common_password_is_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': COMMON_PASSWORD,
            'password2': COMMON_PASSWORD,
        })
        
        errors = json.loads(form.errors.as_json())
        self.assertFalse(form.is_valid())
        self.assertEqual(errors['password2'][0]['code'], "password_too_common")

    def test_entirely_numeric_password_is_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'rand123@mail.com',
            'password1': NUMERIC_PASSWORD,
            'password2': NUMERIC_PASSWORD,
        })
        
        errors = json.loads(form.errors.as_json())
        self.assertFalse(form.is_valid())
        self.assertEqual(errors['password2'][0]['code'], "password_entirely_numeric")

    def test_password_similarity_to_user_is_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'test_user1',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'administrator@example.com',
            'password1': 'administrator123',
            'password2': 'administrator123',
        })
        
        errors = json.loads(form.errors.as_json())
        self.assertFalse(form.is_valid())
        self.assertEqual(errors['password2'][0]['code'], "password_too_similar")