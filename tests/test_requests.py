from django.test import Client
import pytest
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory, APIClient
from visitor.api import VisitorList


pytestmark = pytest.mark.django_db
#
#
# factory = APIRequestFactory()
# user = User.objects.get(username='root')
# view = VisitorList.as_view()
#
# def test_visitor_endpoint():
#     client = APIClient()
#     request = factory.get('/visitor/')
#     force_authenticate(request, user=user)
#     response = view(request)
#     assert response.status_code == 200
#
#     request = factory.get('/visitor/')
#     force_authenticate(request, user=user)
#     response = view(request)
#     assert response.status_code == 404
#
# factory = APIRequestFactory()
# request = factory.post('/visitor/create', {'name:'})
#
# factory = APIRequestFactory()
# user = User.objects.get(username='root')
# view = VisitorList.as_view()
#
# # Make an authenticated request to the view...
# request = factory.get('/visitor/')
# force_authenticate(request, user=user)
# response = view(request)
# assert response.status_code == 404

