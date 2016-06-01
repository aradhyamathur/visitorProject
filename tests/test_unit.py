import unittest
import pytest
from django.test import TestCase
from visitor.models import Visitor
from visitor.serializers import VisitorSerializer
from visitor.api import VisitorList, VisitorDetail
from django.conf.urls import include


class TestClassMy(unittest.TestCase):

    def test_initial(self):
        self.assertEquals('test'.upper(), 'TEST')


@pytest.mark.django_db
class TestVisitorCase(unittest.TestCase):

    def test_can_create_obj(self):
        self.assertTrue(Visitor.objects.create(name='xyz', email='a@a.com',
                        phone_number='+919015670010'), 'obj created')

    def test_serializer(self):

        serializer = VisitorSerializer(data={'name': 'xy', 'email': 'a@a.com',
                                             'phone_number': '+919015670010'})

        self.assertTrue(serializer.is_valid(), 'serializer working')

    def test_fieldcheck(self):
        serializer = VisitorSerializer(data={'name': 'xyz', 'email': ''})
        self.assertFalse(serializer.is_valid(),)


class TestUrlRender(TestCase):

    def test_url_list(self):
        self.assertTrue(VisitorList.as_view())

    def test_url_import(self):
        self.assertTrue(include('visitor.urls'))

    def test_url_detail(self):
        self.assertTrue(VisitorDetail.as_view())


if __name__ == '__main__':
    unittest.main()
