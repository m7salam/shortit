# from django.http import response
import pytest
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from shortit.shortener.api.views import CreateShortUrl
from shortit.users.models import User

pytestmark = pytest.mark.django_db


class TestCreateShortUrlAPIView(APITestCase):

    def test_short_url_generation(self):
        
        """
        Ensure we can create a new short url.
        """
        url = reverse('api:shortener_api:shortit')
        fake = Faker()
        faker_url = fake.url()
        data = {"url": faker_url}
        response = self.client.post(url, data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.status_code == status.HTTP_201_CREATED
