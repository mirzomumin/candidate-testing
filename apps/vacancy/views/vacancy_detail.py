from rest_framework.decorators import (
	api_view,
	authentication_classes,
	permission_classes)
from rest_framework.response import Response
from django.db.models import Case, When, Q, BooleanField
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from vacancy.serializers.vacancy_detail import VacancyDetailSerializer
from vacancy.models import Vacancy


@swagger_auto_schema(method='get')
@api_view(['GET'])
# @authentication_classes([])
@permission_classes([])
@cache_page(60*2)
def get_vacancy_detail(request, pk):
	'''Get full info about current vacancy'''
	vacancy = get_object_or_404(Vacancy, id=pk)
	serializer = VacancyDetailSerializer(
		vacancy, context={'request': request})
	return Response(serializer.data,
		status=HTTP_200_OK)