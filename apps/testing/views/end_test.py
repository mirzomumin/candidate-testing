from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


from testing.serializers.end_test import EndUserResponseSerializer
from testing.models import UserResponse


@swagger_auto_schema(method='patch', request_body=EndUserResponseSerializer)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def end_test(request, response_id):
	'''User ends test'''
	data = request.data
	data['ended_at'] = now()
	data['user'] = request.user.id
	user_response = get_object_or_404(
		UserResponse, id=response_id, is_ended=False)
	serializer = EndUserResponseSerializer(instance=user_response, data=data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response({'response': 'Successfully ended test!',
			'data': serializer.data}, status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)