from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, RecommendationViewSet, RateRecipeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'recipe', RecipeViewSet, basename="recipe")

urlpatterns = [

    path('', include(router.urls)),
    path('rec/', RecommendationViewSet.as_view()),
    path('rate/<int:pk>', RateRecipeViewSet.as_view()),

]
