from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from testing.serializers.start_test import StartUserResponseSerializer
from testing.permissions.is_applied_for_vacancy import IsAppliedForVacancy


@swagger_auto_schema(method='post', request_body=StartUserResponseSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAppliedForVacancy])
def start_test(request, test_id):
	'''User starts test'''
	data = request.data
	data['user'] = request.user.id
	data['started_at'] = now()
	data['test'] = test_id
	serializer = StartUserResponseSerializer(data=data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response({'response': 'Successfully started test!',
			'data': serializer.data}, status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)