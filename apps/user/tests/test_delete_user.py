from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import CustomUser


class DeleteUserTests(APITestCase):
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

	def test_delete_user(self):
		url = reverse('user:delete_user')
		response = self.client.delete(url)
		self.assertEqual(response.status_code, 200)