from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class InventoryTests(APITestCase):
    def test_inventory_list(self):
        """
        Ensure we can list Inventory api.
        """
        models = ['inventory-category', 'inventory-item', 'inventory']
        for model in models:
            url = reverse(
                '{}-list'.format(model),
                kwargs={
                    'version': 'v1'
                }
            )
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
