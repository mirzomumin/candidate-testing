from django.db import models

from helpers.models import BaseModel
from django.conf import settings
# Create your models here.


class Test(BaseModel):
	'''Test for each subcategory of vacancies'''
	title = models.CharField(max_length=255, unique=True)
	description = models.TextField()
	duration_time = models.PositiveIntegerField()

	def __str__(self):
		return f'"{str(self.title)}"'


class Question(BaseModel):
	'''Question of Test'''
	DIFFICULTIES = (
		('E', 'Easy'),
		('M', 'Medium'),
		('H', 'Hard')
	)
	TYPES = (
		('MC', 'Multiple Choice'),
		('TF', 'True/False')
	)
	title = models.TextField(max_length=1000, unique=True)
	point = models.PositiveSmallIntegerField(default=0)
	difficulty = models.CharField(max_length=1, choices=DIFFICULTIES)
	question_type = models.CharField(max_length=2, choices=TYPES)

	# Relations
	test = models.ForeignKey(Test, on_delete=models.CASCADE,
		related_name='questions')

	def __str__(self):
		return str(self.title)


class Option(BaseModel):
	'''Options of each related question'''
	title = models.TextField(max_length=1000)
	is_correct = models.BooleanField(default=False)

	# Relation
	question = models.ForeignKey(Question, on_delete=models.CASCADE,
		related_name='options')

	class Meta:
		unique_together = ('question', 'title')

	def __str__(self):
		return f'{str(self.title)}'


class UserResponse(BaseModel):
	'''Test Responses of User'''
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name='user_responses')
	test = models.ForeignKey(Test, on_delete=models.CASCADE,
		related_name='user_responses')
	started_at = models.DateTimeField(null=True)
	ended_at = models.DateTimeField(null=True)
	is_ended = models.BooleanField(default=False)
	test_result = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return f'Responses of {str(self.user.username)} {str(self.user.last_name)}\
		for test {self.test.title}'


class Answer(BaseModel):
	'''Question Answer responded by user'''
	response = models.ForeignKey(UserResponse, on_delete=models.CASCADE,
		related_name='answers')
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	option = models.ForeignKey(Option, on_delete=models.CASCADE)
