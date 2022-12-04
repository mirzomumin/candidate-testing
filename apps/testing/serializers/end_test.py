from rest_framework import serializers

from testing.models import UserResponse


class EndUserResponseSerializer(serializers.ModelSerializer):
	ended_at = serializers.DateTimeField(required=False)
	test_result = serializers.SerializerMethodField(read_only=True, required=False)
	class Meta:
		model = UserResponse
		fields = ('id', 'user', 'ended_at', 'test_result')
		validators = [
			serializers.UniqueTogetherValidator(
				queryset=model.objects.all(),
				fields=('id', 'ended_at'),
				message=("The test is already ended!")
			)
		]

	def get_test_result(self, obj):
		answers = obj.answers.all()
		for answer in answers:
			if (answer.option.is_correct and\
				answer.option in answer.question.options.all()):
				self.instance.test_result += answer.question.point
		self.instance.save()
		return self.instance.test_result

	def save(self, **kwargs):
		self.instance.is_ended = True
		super().save(**kwargs)