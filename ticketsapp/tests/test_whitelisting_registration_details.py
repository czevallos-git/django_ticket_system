from django.test import TestCase
import re


class TestRegistrationDetails(TestCase):
    def test_email_format(self):
        email = "ab@test.com"
        # The most common email format will have the following form: (username)@(domainname).(top_level_domain)
        # The username allows the special characters ".", "_", and "-", but not at the beginning or before "@"
        # The domain allows any alphanumeric character
        # There can be more than one top level domains with two or more letters each separated by one dot
        regex = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        z = re.match(regex, email)

        self.assertTrue(z)
