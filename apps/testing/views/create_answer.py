from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from testing.serializers.create_answer import CreateAnswerSerializer
from testing.models import Answer


@swagger_auto_schema(method='post', request_body=CreateAnswerSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_answer(request):
	'''Create answer to question'''
	serializer = CreateAnswerSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response({'response': 'Successfully answered!',
			'data': serializer.data}, status=HTTP_201_CREATED)
	return Response('Bad Request!', status=HTTP_400_BAD_REQUEST)