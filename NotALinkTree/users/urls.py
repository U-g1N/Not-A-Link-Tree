from django.urls import path, include
from users.views import signup, login, get_profile
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'custom-viewset', UserViewSet)

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('profile/', get_profile),
    path('', include(router.urls)),
]
