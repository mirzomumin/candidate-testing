from rest_framework import serializers
from django.shortcuts import get_object_or_404

from vacancy.models import Vacancy
from testing.models import UserResponse

from testing.serializers.test_result import TestResultSerializer


class VacanciesApplied(serializers.ModelSerializer):
	test = serializers.SerializerMethodField(read_only=True)
	test_result = serializers.SerializerMethodField(read_only=True)
	category = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Vacancy
		fields = ('id', 'category', 'title', 'company_name', 'short_description',\
		'test', 'test_result')
		read_only_fields = fields

	def get_test(self, obj):
		return obj.test.title

	def get_category(self, obj):
		return obj.category.name

	def get_test_result(self, obj):
		user = self.context['request'].user.id
		test = obj.test.id
		test_result = get_object_or_404(
			UserResponse, test=test,
			user=user, is_ended=True)
		serializer = TestResultSerializer(test_result)
		return serializer.data