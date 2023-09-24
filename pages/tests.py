from django.test import TestCase
from django.urls import reverse

class HomePageTesting (TestCase) :


    def test_home_by_url_name(self) :
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_home_by_content(self) :
        response = self.client.get(reverse('home'))
        self.assertContains(response,'HOME')

    def test_home_by_url (self) :
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_template (self) :
        response = self.client.get('/')
        self.assertTemplateUsed(response,"home.html")

    
