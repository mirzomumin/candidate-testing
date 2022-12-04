from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import CustomUser


class ChangeUserPasswordTests(APITestCase):
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
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

	def test_change_password_success(self):
		url = reverse('user:change_password')
		data = {'old_password': 'password', 'new_password': 'new_password'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 200)

	def test_change_password_fail(self):
		url = reverse('user:change_password')
		data = {'old_password': 'incorrect', 'new_password': 'new_password'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.data['response'], 'Invalid old password!')