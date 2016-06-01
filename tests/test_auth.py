from visitorProject import settings
from django.test import TestCase

# test for REST framework authorisation settings


class TestAuth(TestCase):

    def test_auth(self):
        self.assertEquals(settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION'],
                          tuple(('rest_framework.authentication.BasicAuthentication',)))
