from django.test import TestCase
from django.urls import reverse


class MyTestClass(TestCase):
    # test case must start with test_
    def test_demo_view(self):
        # ok status .
        response = self.client.get(reverse('demo_url'))
        self.assertEqual(response.status_code, 200)

    def test_demo_view1(self):
        # F status .
        response = self.client.get(reverse('demo_url1'))
        self.assertEqual(response.status_code, 400)

    def test_demo_view2(self):
        # E status .
        response = self.client.get(reverse('demo_url2'))
        self.assertEqual(response.status_code, 200)
