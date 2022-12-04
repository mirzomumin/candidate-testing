from rest_framework import serializers

from testing.models import Answer


class CreateAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('id', 'response', 'question', 'option')
		validators = [
			serializers.UniqueTogetherValidator(
				queryset=model.objects.all(),
				fields=('response', 'question'),
				message=("Answer for this question already exsits!")
			)
		]