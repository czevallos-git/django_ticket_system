from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ticketsapp.views import home_page
from ticketsapp.auth import login_page, register_page


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, home_page)

    def test_login_url_is_resolves(self):
        url = reverse('login_page')
        self.assertEquals(resolve(url).func, login_page)
    
    def test_register_url_is_resolves(self):
        url = reverse('register_page')
        self.assertEquals(resolve(url).func, register_page)