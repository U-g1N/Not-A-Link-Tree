from rest_framework import serializers
from enum import unique
# from users.models import User


class createUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(required=True)
