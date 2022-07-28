from rest_framework import serializers
from users.models import Links, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"
