import json

from django.test import Client, TestCase


class HealthEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_v1(self) -> None:
        response = self.client.get("/api/v1/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_settings_v1(self) -> None:
        response = self.client.get("/api/v1/settings/")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("service_name", payload)
        self.assertIn("environment", payload)
        self.assertIn("api_v1_prefix", payload)
