from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=32, required=False,
                                  validators=[UniqueValidator(CustomUser.objects.all())])
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'email', 'phone', 'about_me', 
                  'avatar', 'linkedin', 'github', 'telegram', 'resume']
        extra_kwargs = {
            'username': {'required': False},
            'last_name': {'required': False}
        }
        read_only_fields = ['email']