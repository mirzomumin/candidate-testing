from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


from vacancy.models import Vacancy


class VacancyDetailSerializer(serializers.ModelSerializer):
	phone = PhoneNumberField(read_only=True)
	is_applied = serializers.SerializerMethodField(default=None, read_only=True)
	class Meta:
		model = Vacancy
		fields = ('title', 'company_name', 'short_description', 'duties',
			'requirements', 'offers', 'contact_person', 'phone', 'email',
			'address', 'website', 'test', 'is_applied', 'created_at')

	def get_is_applied(self, obj):
		user = self.context['request'].user
		if user.is_authenticated:
			if user in obj.users.all():
				return True
			return False
		return None