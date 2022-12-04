from rest_framework import serializers

from testing.models import Answer


class UpdateAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('id', 'response', 'question', 'option')