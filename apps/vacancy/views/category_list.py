from rest_framework.decorators import (
	api_view,
	permission_classes,
	authentication_classes)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from drf_yasg.utils import swagger_auto_schema

from vacancy.models import Category
from vacancy.serializers.category_list import CategorySerializer


@swagger_auto_schema(method='get')
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_category_list(request):
	'''Get all categories and subcategories of vacancies'''
	categories = Category.objects.filter(parent=None)\
	.prefetch_related('subcategories', 'subcategories__subcategories')\
	.all()
	serializer = CategorySerializer(categories, many=True)
	return Response(serializer.data, status=HTTP_200_OK)