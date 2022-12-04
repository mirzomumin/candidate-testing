from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from user.models import CustomUser
from user.permissions.is_owner import IsOwner
from user.serializers.profile import ProfileSerializer
from user.tasks import auto_delete_resume


@swagger_auto_schema(method='put', request_body=ProfileSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsOwner])
@parser_classes([MultiPartParser])
def update_profile(request, user_id):
    '''Edit profile of user_id'''
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = ProfileSerializer(instance=user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(
            {'response': 'Successfully updated!',
            'data': serializer.data},
            status=HTTP_200_OK)
    return Response(serializer.errors, 
                    status=HTTP_400_BAD_REQUEST)