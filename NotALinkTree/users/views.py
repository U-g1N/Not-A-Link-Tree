from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer

# Create your views here.


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
    # User.objects.create(name=request.data.get("name"),
    #                     email=request.data.get("email"),
    #                     password=request.data.get("password"))
    # return Response("Created", status=200)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_user(request):
    try:
        user = User.objects.get(email=request.data.get("email"))
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response(serializer.data)

    # user = User.objects.get(
    #     email=request.data.get("email"),
    # )
    # return Response({"user": user.name, "uuid": user.uuid}, status=200)
