from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User, Links
from users.serializers import UserSerializer, LinksSerializer
from rest_framework.exceptions import MethodNotAllowed

# Create your views here.


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
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
def login(request):
    try:
        user = User.objects.get(email=request.data.get("email"), password=request.data.get("password"))
        token = RefreshToken.for_user(user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response({
            "refresh": str(token),
            "access": str(token.access_token),
            "data": serializer.data
        })

    # user = User.objects.get(
    #     email=request.data.get("email"),
    # )
    # return Response({"user": user.name, "uuid": user.uuid}, status=200)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_profile(request):
    user = User.objects.get(email = request.user)
    serializer = UserSerializer(user)
    return Response({
            "data": serializer.data
        })

# write a viewset for user object
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email = request.user)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(
            'GET', detail='Method "GET" not allowed with lookup.')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(
            'DELETE', detail='Method "DELETE" not allowed.')

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def uploadlink(request):
    serialized = LinksSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        user = Links.objects.get(email = request.user)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(
            'GET', detail='Method "GET" not allowed with lookup.')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(
            'DELETE', detail='Method "DELETE" not allowed.')