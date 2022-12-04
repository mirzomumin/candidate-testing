from rest_framework.decorators import (
	api_view,
	permission_classes,
	authentication_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from drf_yasg.utils import swagger_auto_schema

from vacancy.models import Vacancy
from vacancy.serializers.vacancies_applied import VacanciesApplied


@swagger_auto_schema(method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vacancies_applied(request):
	'''Get all vacancies applied for by user'''
	user = request.user.id
	vacancies_applied = Vacancy.objects.filter(users=user).all()
	serializer = VacanciesApplied(vacancies_applied,
		context={'request': request}, many=True)
	return Response(serializer.data, status=HTTP_200_OK)