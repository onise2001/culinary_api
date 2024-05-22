from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'recipe', RecipeViewSet, basename="recipe")

urlpatterns = [

    path('', include(router.urls)),

]
