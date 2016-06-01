import pytest
from django.contrib.auth.models import User

# test database user

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUser(object):

    @pytest.fixture(autouse=True)
    def create_demo_user(self, db):
       test_user = User.objects.create_superuser(username='abc', password='abc', email='abc@abc.com')

    @pytest.mark.django_db
    def test_my_user(self):
        me = User.objects.get(username='abc')
        assert me.is_superuser
