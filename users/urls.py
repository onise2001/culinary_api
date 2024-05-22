from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUser, CreateChef
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)
router.register(r'signup', CreateUser, basename="signup")
router.register(r'chef', CreateChef, basename="createchef")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", obtain_auth_token)
]
