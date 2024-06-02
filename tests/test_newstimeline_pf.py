import time
from django.test import TestCase
from rest_framework.test import APIClient


class NewsTimeLineTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/news/'

    def test_news_timeline_qps(self):
        num_requests = 200
        start_time = time.time()

        for _ in range(num_requests):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)

        end_time = time.time()
        total_time = end_time - start_time
        qps = num_requests / total_time
        print(f"QPS: {qps}")
