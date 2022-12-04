from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import CustomUser


class GetProfileTests(APITestCase):
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
		self.id = response.data['data']['id']
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

	def test_get_profile_success(self):
		url = reverse('user:get_profile', kwargs={'user_id': self.id})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_get_profile_fail(self):
		url = reverse('user:get_profile', kwargs={'user_id': 100})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)