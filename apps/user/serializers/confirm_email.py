from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from django.shortcuts import get_object_or_404

from user.models import CustomUser

class ConfirmationCodeSerializer(serializers.Serializer):
	'''Confirmation code'''
	confirmation_code = serializers.IntegerField(required=True)