from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTesting(TestCase) :
    username = 'new_user'
    email = 'new_user@gmail.com'


    def test_signup_url_by_name (self) :
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200) 

    def test_signup_url (self) :
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200) 

    def test_signup_templates(self) :
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response,'registration/signup.html')

    def test_signup_object(self) :
        User = get_user_model().objects.create_user(self.username,self.email)
            
        
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)
    
