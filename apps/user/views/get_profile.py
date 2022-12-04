from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from user.models import CustomUser
from user.permissions.is_owner import IsOwner
from user.serializers.profile import ProfileSerializer


@swagger_auto_schema(method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def get_profile(request, user_id):
    '''Get profile by user_id'''
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = ProfileSerializer(instance=user)
    return Response(
            {'response': 'Successfully updated!',
            'data': serializer.data},
            status=HTTP_200_OK)

