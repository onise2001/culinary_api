from rest_framework import filters
from .models import Recipe
from collections import Counter

class RecommendationFilter(filters.BaseFilterBackend):


    def filter_queryset(self, request, queryset, view):

        my_recipes = queryset.filter(user=request.user)
        all_ingredients = Counter()
        for recipe in my_recipes:
            for ingredient in recipe.ingredients.all():
               all_ingredients[ingredient.name] +=1

        most_frequent = all_ingredients.most_common()[0][0]
        
        
        with_frequent = Counter()
        for recipe in my_recipes:
            ingredient_names = [ingredient.name for ingredient in recipe.ingredients.all()]    
            if most_frequent in ingredient_names:
                for ingredient in recipe.ingredients.all():
                   if most_frequent != ingredient.name:
                       with_frequent[ingredient.name] += 1

        second_frequent = with_frequent.most_common()[0][0]


        recommendations = []

        for recipe in Recipe.objects.all():
            #if recipe.user != request.user:
            ingredient_names = [ingredient.name for ingredient in recipe.ingredients.all() ]
            if most_frequent in ingredient_names and second_frequent in ingredient_names:
                recommendations.append(recipe.id)

        
        filterd_recipes = Recipe.objects.filter(pk__in=recommendations)

        return filterd_recipes