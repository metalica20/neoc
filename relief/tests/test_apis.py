from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RealtimeTests(APITestCase):
    def test_realtime_list(self):
        """
        Ensure we can list relief apis.
        """
        names = ['relief-release', 'relief-flow']
        for name in names:
            url = reverse(
                '{}-list'.format(name),
                kwargs={
                    'version': 'v1'
                }
            )
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
