from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserViewSetTest(APITestCase):
    LIST_URL = "/users/users/"

    def test_list(self):
        user = baker.make(User)
        self.client.force_authenticate(user)

        users = baker.make(User, _quantity=10)

        response = self.client.get(self.LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 11)
