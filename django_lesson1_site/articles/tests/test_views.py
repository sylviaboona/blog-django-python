from django.conf.urls import url
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserRegistrationViewTest(TestCase):

    def test_register_page_rendering(self):
        """
        Register page is rendered on a get request
        """
        #define the url for the get request
        url = reverse('register-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register_user.html')
    
    def test_register_user(self):
        """
        A users details are posted to the database
        """
        url = reverse('register-user')
        response = self.client.post(url, {'username':'sylvy',  'password':'12345', 'email': 'syl@gmail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login-user'), 302)
    
    def test_register_user_without_username(self):
        """
        If no user name, form is not posted 
        """
        url = reverse('register-user')
        response = self.client.post(url, {'username':'',  'password':'12345', 'email': 'syl@gmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['usernameErr'], 'username is empty')
    
    def test_logged_in_user_shouldnt_register(self):
        """
        A logged in user shouldnt access the registration page
        """
        user = User.objects.create_user(username='boona', email='boona@gmail.com',password='12345')
        self.client.login(username='boona', password='12345')
        url = reverse('register-user')
        response = self.client.post(url, {'username':'pola',  'password':'12345', 'email': 'pola@gmail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('all-articles-url'), 302)







