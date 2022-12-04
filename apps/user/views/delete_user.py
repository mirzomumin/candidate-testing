from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_200_OK)
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='delete')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
	user = request.user
	if user is not None:
		operation = user.delete()
		data = {}
		if operation:
			data['response'] = 'Successfully user deleted!'
			return Response(data=data, status=HTTP_200_OK)
		data['response'] = 'User delete failed!'
		return Response(data=data, status=HTTP_400_BAD_REQUEST)