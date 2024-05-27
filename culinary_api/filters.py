from rest_framework import filters
from .models import Recipe
from collections import Counter

class RecommendationFilter(filters.BaseFilterBackend):


    def filter_queryset(self, request, queryset, view):

        my_recipes = queryset.filter(user=request.user)
        
        if len(my_recipes) > 0:
            all_ingredients = Counter([ingredient.name for recipe in my_recipes for ingredient in recipe.ingredients.all()])

            if len(all_ingredients.most_common()) > 0: 
                most_frequent = all_ingredients.most_common()[0][0]
                
                with_frequent = Counter([ingredient.name for recipe in my_recipes for ingredient in recipe.ingredients.all() if most_frequent in [ingredient.name for ingredient in recipe.ingredients.all()] and most_frequent != ingredient.name])
               
                if len(with_frequent.most_common()) > 0:
                    second_frequent = with_frequent.most_common()[0][0]
            
                    recommendations = [recipe.id for recipe in queryset.all() if most_frequent in [ingredient.name for ingredient in recipe.ingredients.all()] and second_frequent in [ingredient.name for ingredient in recipe.ingredients.all()]  and request.user != recipe.user]
            
                    filterd_recipes = queryset.filter(pk__in=recommendations)
            
                    return filterd_recipes
                
                recommendations = [recipe.id for recipe in queryset.all() if most_frequent in [ingredient.name for ingredient in recipe.ingredients.all()]]
        
                filterd_recipes = queryset.filter(pk__in=recommendations)
        
                return filterd_recipes                
        
        return []

  

class RecipeNameFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name')
        if name:
            filtered_queryset = queryset.filter(name__contains=name.capitalize())
            #print(request.query_params)
            return filtered_queryset
        
        return queryset
  
  
  
    # def filter_queryset(self, request, queryset, view):

    #     my_recipes = queryset.filter(user=request.user)
    #     all_ingredients = Counter()
    #     for recipe in my_recipes:
    #         for ingredient in recipe.ingredients.all():
    #            all_ingredients[ingredient.name] +=1

    #     most_frequent = all_ingredients.most_common()[0][0]
        
        
    #     with_frequent = Counter()
    #     for recipe in my_recipes:
    #         ingredient_names = [ingredient.name for ingredient in recipe.ingredients.all()]    
    #         if most_frequent in ingredient_names:
    #             for ingredient in recipe.ingredients.all():
    #                if most_frequent != ingredient.name:
    #                    with_frequent[ingredient.name] += 1

    #     second_frequent = with_frequent.most_common()[0][0]


    #     recommendations = []

    #     for recipe in Recipe.objects.all():
    #         #if recipe.user != request.user:
    #         ingredient_names = [ingredient.name for ingredient in recipe.ingredients.all() ]
    #         if most_frequent in ingredient_names and second_frequent in ingredient_names:
    #             recommendations.append(recipe.id)

        
    #     filterd_recipes = Recipe.objects.filter(pk__in=recommendations)

    #     return filterd_recipes