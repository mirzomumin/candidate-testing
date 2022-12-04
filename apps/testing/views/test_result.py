from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


from testing.serializers.test_result import TestResultSerializer
from testing.models import UserResponse


@swagger_auto_schema(method='get')
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_test_result(request, response_id):
	'''Get Test Result'''
	user_response = get_object_or_404(UserResponse, id=response_id)
	serializer = TestResultSerializer(user_response)
	return Response(serializer.data, status=HTTP_200_OK)