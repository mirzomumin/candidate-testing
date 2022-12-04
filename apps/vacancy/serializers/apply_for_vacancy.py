from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable

from vacancy.models import Vacancy


class ApplyForVacancySerializer(serializers.ModelSerializer):
	test = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Vacancy
		fields = ('id', 'test')

	def get_test(self, obj):
		return self.instance.test.id

	def validate(self, attrs):
		vacancy = self.instance
		request = self.context.get("request")
		user = request.user
		if vacancy.is_active == False:
			raise NotAcceptable('This vacancy is not active!')
		if user in vacancy.users.all():
			raise NotAcceptable('You already has applied for this vacancy!')
		return {'response': 'Successfully applied for this vacancy!'}

	def save(self, **kwargs):
		request = self.context.get("request")
		user = request.user.id
		self.instance.users.add(user)
		super().save(**kwargs)