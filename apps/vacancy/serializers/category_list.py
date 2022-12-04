from rest_framework import serializers

from vacancy.models import Category


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name', 'subcategories')

	def get_fields(self):
		fields = super(CategorySerializer, self).get_fields()
		fields['subcategories'] = CategorySerializer(many=True)
		return fields

	def to_representation(self, instance):
		result = super(CategorySerializer, self).to_representation(instance)
		result = dict([(key, value) for key, value in result.items()\
			if value not in (None, [], {}, ())])
		return result