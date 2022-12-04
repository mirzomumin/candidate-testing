from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import CustomUser


class SignOutTests(APITestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(
			username='Nick',
			last_name='Freeman',
			email='testuser@gmail.com',
			password='password',
			is_active=True
		)
		url = reverse('user:sign_in')
		data = {'email': 'testuser@gmail.com', 'password': 'password'}
		response = self.client.post(url, data)
		access_token = response.data['data']['tokens']['access']
		self.refresh_token = response.data['data']['tokens']['refresh']
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

	def test_sign_out(self):
		url = reverse('user:sign_out')
		response = self.client.post(url, {'refresh': self.refresh_token})
		self.assertEqual(response.status_code, 204)