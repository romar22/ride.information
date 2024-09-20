from rest_framework.test import APITestCase
from django.urls import reverse
from users.test.factories import UserFactory
from rides.test.factories import RideFactory
from faker import Faker

fake = Faker()

class RidesTestCase(APITestCase):

    def test_list(self):
        url = reverse('rides')
        instance = UserFactory()
        RideFactory.create_batch(20)

        self.client.force_authenticate(user=instance)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
