from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class IncidentTests(APITestCase):
    def test_list(self):
        """
        Ensure we can list incidents.
        """
        url = reverse(
            'incident-list',
            kwargs={
                'version': 'v1'
            }
        )
        response = self.client.get(url, {'expand': '~all'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
