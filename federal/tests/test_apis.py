from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FederalTests(APITestCase):
    def test_federal_list(self):
        """
        Ensure we can list federals.
        """
        models = ['province', 'district', 'municipality', 'ward']
        for model in models:
            url = reverse(
                '{}-list'.format(model),
                kwargs={
                    'version': 'v1'
                }
            )
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_district_geojson(self):
        """
        Ensure geojson is generated.
        """
        models = ['province', 'district', 'municipality', 'ward']
        for model in models:
            url = reverse(
                '{}-list'.format(model),
                kwargs={
                    'version': 'v1'
                }
            )
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
