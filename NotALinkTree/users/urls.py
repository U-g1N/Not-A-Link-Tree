from django.urls import path, include
from users.views import signup, login, get_profile, uploadlink
from rest_framework import routers

from .views import UserViewSet, LinksViewSet

router = routers.DefaultRouter()
router.register(r'custom-viewset', UserViewSet)
router.register(r'custom-viewset', LinksViewSet)

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('profile/', get_profile),
    path('uploadlink/', uploadlink),
    path('', include(router.urls)),
]
