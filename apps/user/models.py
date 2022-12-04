import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError

# from testing.models import Test
from vacancy.models import Vacancy
# Create your models here.

def upload_to(instance, filename):
	return f'media/{instance.email}/{filename}'


def validate_resume(value):
	max_size = 1024 * 1024 * 4
	ext = os.path.splitext(value.name)[1].lower()
	valid_extensions = ['.pdf']
	if not ext in valid_extensions or value.size > max_size:
		raise ValidationError('Unsupported file extension or file is bigger than 5MB.')


def validate_avatar(value):
	max_size = 1024 * 1024
	ext = os.path.splitext(value.name)[1].lower()
	valid_extensions = ['.jpg', '.png', '.jpeg']
	if not ext in valid_extensions or value.size > max_size:
		raise ValidationError('Unsupported file extension or file is bigger than 1MB.')


class CustomUser(AbstractUser):
	'''Customized User for E-commerce project'''
	ROLES = (
		('HRM', 'Human Resource Manager'),
		('TM', 'Test Maker'),
		('C', 'Candidate')
	)
	email = models.EmailField(blank=False, null=False, unique=True)
	confirmation_code = models.PositiveIntegerField(blank=True, null=True)
	verified_at = models.DateTimeField(null=True, blank=True)

	# User Profile Info
	username = models.CharField('first_name', max_length=128, unique=False)
	last_name = models.CharField('last_name', max_length=128)
	phone = PhoneNumberField(blank=True, null=True, unique=True)
	about_me = models.TextField(blank=True, null=True)
	avatar = models.ImageField(upload_to=upload_to, validators=[validate_avatar], blank=True, null=True)
	resume = models.FileField(upload_to=upload_to, validators=[validate_resume], blank=True, null=True)
	linkedin = models.URLField(max_length=255, blank=True, null=True)
	telegram = models.CharField(max_length=255, blank=True, null=True)
	github = models.URLField(max_length=255, blank=True, null=True)
	role = models.CharField(max_length=3, choices=ROLES, default='C')
	# Relations
	# test = models.ForeignKey(Test, on_delete=models.CASCADE,
	# 	related_name='users')
	vacancies = models.ManyToManyField(Vacancy, blank=True,
		related_name='users')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'last_name']

	def tokens(self):
		'''Return access and refresh tokens'''
		refresh = RefreshToken.for_user(self)
		return{
			'refresh':str(refresh),
			'access':str(refresh.access_token)
		}

	def delete_resume(self):
		self.resume.delete()