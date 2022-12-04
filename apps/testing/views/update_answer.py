from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from testing.serializers.update_answer import UpdateAnswerSerializer
from testing.models import Answer


@swagger_auto_schema(method='patch', request_body=UpdateAnswerSerializer)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_answer(request):
	'''Update answer of question'''
	answer = get_object_or_404(
		Answer,
		response__id=request.data['response'],
		question__id=request.data['question'])
	serializer = UpdateAnswerSerializer(instance=answer, data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response(
			{'response': 'Successfully updated!',
			'data': serializer.data},
			status=HTTP_201_CREATED)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)