from django.urls import path
from users.views import create_user, get_user

urlpatterns = [
    path('create-user/', create_user),
    path('get-user/', get_user),
]
