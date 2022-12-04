from rest_framework import serializers

from testing.models import Test, Question, Option


class OptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Option
		fields = ('id', 'title')
		read_only_fields = fields


class QuestionSerializer(serializers.ModelSerializer):
	options = OptionSerializer(many=True, read_only=True)
	class Meta:
		model = Question
		fields = ('id', 'title', 'point', 'difficulty', 'options')
		read_only_fields = fields


class TestSerializer(serializers.ModelSerializer):
	questions = QuestionSerializer(many=True, read_only=True)
	class Meta:
		model = Test
		fields = ('id', 'title', 'description', 'duration_time',
			'questions')
		read_only_fields = fields