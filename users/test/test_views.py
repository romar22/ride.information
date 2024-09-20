from rest_framework.test import APITestCase
from django.urls import reverse
from .factories import UserFactory
from django.contrib.auth.hashers import make_password
from faker import Faker

fake = Faker()

class LoginTestCase(APITestCase):

    def test_login(self):
        url = reverse('login')
        password = fake.password()
        instance = UserFactory()
        instance.password = make_password(password)
        instance.save()

        resp = self.client.post(url, {
            'email': instance.email,
            'password': password
        }, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, {
            'refresh': resp.data['refresh'],
            'access': resp.data['access']
        })