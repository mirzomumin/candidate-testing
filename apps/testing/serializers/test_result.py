from rest_framework import serializers

from testing.models import UserResponse


class TestResultSerializer(serializers.ModelSerializer):
	total_point = serializers.SerializerMethodField(read_only=True)
	test_result_in_percent = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = UserResponse
		fields = ('id', 'test_result', 'test_result_in_percent', 'total_point')
		read_only_fields = fields

	def get_total_point(self, obj):
		total_point = 0
		questions = obj.test.questions.all()
		for question in questions:
			total_point += question.point
		return total_point


	def get_test_result_in_percent(self, obj):
		result_in_percent = \
		round(obj.test_result / self.get_total_point(obj) * 100, 2)
		return result_in_percent