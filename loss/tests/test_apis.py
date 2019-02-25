from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LossTests(APITestCase):
    def test_loss_list(self):
        """
        Ensure we can list loss.
        """
        models = ['loss', 'infrastructure_type', 'livestock_type']
        for model in models:
            url = reverse(
                '{}-list'.format(model),
                kwargs={
                    'version': 'v1'
                }
            )
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
