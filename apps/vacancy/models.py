from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from helpers.models import BaseModel
# from user.models import CustomUser
from testing.models import Test
# Create your models here.

class Category(BaseModel):
	'''Category of each vacancy'''
	name = models.CharField(max_length=128, unique=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE,
		null=True, blank=True, related_name='subcategories')

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return f'{self.name}'


class Vacancy(BaseModel):
	'''Vacancy for users looking for job'''
	title = models.CharField(max_length=100)
	company_name = models.CharField(max_length=100)
	short_description = models.CharField(max_length=100)
	duties = models.TextField(max_length=1000)
	requirements = models.TextField(max_length=1000)
	offers = models.TextField(max_length=1000)
	contact_person = models.CharField(max_length=64)
	phone = PhoneNumberField()
	email = models.EmailField()
	address = models.URLField()
	website = models.URLField()
	is_active = models.BooleanField(default=True)

	# Relations
	category = models.ForeignKey(Category, on_delete=models.CASCADE,
		null=True, blank=True)
	test = models.ForeignKey(Test, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='vacancies')

	class Meta:
		verbose_name_plural = 'vacancies'

	def __str__(self):
		return f'Company: {self.company_name}.\
		Title: {self.title}'