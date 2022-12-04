from rest_framework import serializers
from django.shortcuts import get_object_or_404

from testing.models import Test, UserResponse

class TestInfoSerializer(serializers.ModelSerializer):
	questions_count = serializers.IntegerField()
	is_passed = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Test
		fields = ('id', 'title', 'description', 'duration_time',
			'questions_count', 'is_passed')
		read_only_fields = fields

	def get_is_passed(self, obj):
		user = self.context['request'].user
		user_response = UserResponse.objects.filter(
			user=user.id,
			test=obj['id'],
			is_ended=True)
		if user_response.exists():
			return True
		return False