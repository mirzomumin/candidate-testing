from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import CustomUser


class SignInTests(APITestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(
			username='Nick',
			last_name='Freeman',
			email='testuser@gmail.com',
			password='password',
			is_active=True
		)

	def test_fail_sign_in(self):
		url = reverse('user:sign_in')
		data = {'email': 'incorrect', 'password': 'incorrect'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 400)

	def test_success_sign_in(self):
		url = reverse('user:sign_in')
		data = {'email': 'testuser@gmail.com', 'password': 'password'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 200)
		self.assertIn('tokens', response.data['data'])
		self.assertIn('id', response.data['data'])