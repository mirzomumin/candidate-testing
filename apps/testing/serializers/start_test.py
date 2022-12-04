from rest_framework import serializers

from testing.models import UserResponse


class StartUserResponseSerializer(serializers.ModelSerializer):
	started_at = serializers.DateTimeField(required=False)
	# ended_at = serializers.DateTimeField(required=False)
	class Meta:
		model = UserResponse
		fields = ('id', 'user', 'started_at', 'test')
		validators = [
			serializers.UniqueTogetherValidator(
				queryset=model.objects.all(),
				fields=('user', 'test'),
				message=("The test is already started!")
			)
		]