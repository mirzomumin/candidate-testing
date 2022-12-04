from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.cache import cache_page

from testing.serializers.test_questions import QuestionSerializer
from testing.models import Question, Option


@swagger_auto_schema(method='get')
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@cache_page(15 * 60)
def get_test_questions(request, pk):
	'''Get questions of related test'''
	test_questions = Question.objects.filter(test__id=pk)\
	.prefetch_related('options')\
	.order_by('?').all()
	serializer = QuestionSerializer(test_questions, many=True)
	return Response(serializer.data, status=HTTP_200_OK)