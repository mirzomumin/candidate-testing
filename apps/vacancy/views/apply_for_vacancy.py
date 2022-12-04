from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from vacancy.serializers.apply_for_vacancy import ApplyForVacancySerializer
from vacancy.models import Vacancy


@swagger_auto_schema(method='patch', request_body=ApplyForVacancySerializer)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def apply_for_vacancy(request, pk):
	'''User applies for vacancy'''
	vacancy = get_object_or_404(Vacancy, id=pk)
	serializer = ApplyForVacancySerializer(
		instance=vacancy,
		data=request.data,
		context={'request': request})
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response({'response': 'Successfully applied!',
			'data': serializer.data}, status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)