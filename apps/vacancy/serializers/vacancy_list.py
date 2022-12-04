from rest_framework import serializers

from vacancy.models import Vacancy


class VacancyListSerializer(serializers.ModelSerializer):
	is_applied = serializers.SerializerMethodField(read_only=True, default=None)
	category = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Vacancy
		fields = ('id', 'category', 'title', 'short_description',
		'is_applied', 'created_at')
		read_only_fields = fields

	def get_category(self, obj):
		return obj.category.name

	def get_is_applied(self, obj):
		user = self.context['request'].user
		if user.is_authenticated:
			if user in obj.users.all():
				return True
			return False
		return None
