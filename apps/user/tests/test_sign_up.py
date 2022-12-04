from rest_framework.test import APITestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404

from user.models import CustomUser


class SignUpTests(APITestCase):
	def test_sign_up_success_response(self):
		url = reverse('user:sign_up')
		data = {
			'username': 'Michael',
			'last_name': 'Wood',
			'email': 'testuser@gmail.com',
			'phone': '+998970049812',
			'password': '1sakura1'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 201)

	def test_sign_up_fail_response(self):
		url = reverse('user:sign_up')
		data = {}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 400)

		# Unique email
		user = CustomUser.objects.create(username='Nick', last_name='Freeman',
			email='admin@gmail.com')
		response = self.client.post(url, {'email': 'admin@gmail.com'})
		self.assertEqual(response.status_code, 400)

	def test_confirm_success_response(self):
		email = self._sign_up()['email']
		url = reverse('user:confirm')
		user = get_object_or_404(CustomUser, email=email)
		response = self.client.get(f"{url}?confirmation_code={user.confirmation_code}")
		self.assertEqual(response.status_code, 200)

	def test_confirm_fail_response(self):
		url = reverse('user:confirm')
		response = self.client.get(f"{url}?confirmation_code=confirmation-code")
		self.assertEqual(response.status_code, 400)

	def _sign_up(self):
		url = reverse('user:sign_up')
		data = {
			'username': 'Michael',
			'last_name': 'Wood',
			'email': 'testuser@gmail.com',
			'phone': '+998970049812',
			'password': '1sakura1'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 201)
		self.assertIn('email', response.data)
		return response.data