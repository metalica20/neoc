from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RealtimeTests(APITestCase):
    def test_realtime_list(self):
        """
        Ensure we can list realtime api.
        """
        models = ['earthquake', 'river', 'rain']
        for model in models:
            url = reverse(
                '{}-list'.format(model),
                kwargs={
                    'version': 'v1'
                }
            )
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
