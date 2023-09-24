from django.test import TestCase
from django.urls import reverse

class HomePageTesting (TestCase) :


    def test_home_by_url_name(self) :
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
