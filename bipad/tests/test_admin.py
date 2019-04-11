from django.test import TestCase


class AdminTest(TestCase):
    def test_running(self):
        resp = self.client.get('/en/admin/login/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/ne/admin/login/')
        self.assertEqual(resp.status_code, 200)
