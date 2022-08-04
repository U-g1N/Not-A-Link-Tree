from django.urls import path
from users.views import signup, login, get_profile

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('profile/', get_profile),
]
