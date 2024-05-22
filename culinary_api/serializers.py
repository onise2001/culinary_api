from rest_framework import serializers
from .models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Ingredient
        fields = "__all__"





class RecipeSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = "__all__"


    
    def create(self, validated_data):
        print("In Create")
        ingredients = validated_data.pop('ingredients')

        recipe = Recipe(**validated_data)
        recipe.save()

        for ingredient in ingredients:
            #print(ingredient)
            ingredient = Ingredient.objects.create(name=ingredient['name'], amount=ingredient['amount'])
            ingredient.save()
            recipe.ingredients.add(ingredient)

        return recipe
    

    def update(self,instance, validated_data):
        print(instance.ingredients)
        instance.ingredients.clear()

        print(validated_data)

        new_ingredients = validated_data.pop('ingredients')
        instance = super(RecipeSerializer, self).update(instance, validated_data)
        

        for ingredient in new_ingredients:
            old_ingredient = Ingredient.objects.get(pk=ingredient['id'])
            old_ingredient.name = ingredient['name']
            old_ingredient.amount = ingredient['amount']
            old_ingredient.save()
            instance.ingredients.add(old_ingredient)
        instance.save()
        return instance