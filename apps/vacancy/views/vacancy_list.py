from rest_framework.decorators import (
	api_view,
	permission_classes,
	authentication_classes)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.cache import cache_page

from vacancy.serializers.vacancy_list import VacancyListSerializer
from vacancy.models import Vacancy


@swagger_auto_schema(method='get')
@api_view(['GET'])
# @authentication_classes([])
@permission_classes([])
@cache_page(60 * 2)
def get_vacancy_list(request):
	'''Get all vacancies posted to site'''
	vacancies = Vacancy.objects.select_related('category').all()
	serializer = VacancyListSerializer(
		vacancies, context={'request': request}, many=True)
	return Response(serializer.data,
		status=HTTP_200_OK)