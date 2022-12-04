from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.cache import cache_page

from testing.serializers.test_info import TestInfoSerializer
from testing.models import Test


@swagger_auto_schema(method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60 * 1)
def get_test_info(request, pk):
	'''Get info about test of related vacancy'''
	queryset = Test.objects.prefetch_related('vacancies__id')\
	.values('id', 'title', 'description', 'duration_time').annotate(
			questions_count=Count('questions')
		)
	test_info = get_object_or_404(queryset, id=pk)
	serializer = TestInfoSerializer(test_info, context={'request': request})
	return Response(serializer.data, status=HTTP_200_OK)