from rest_framework import serializers
from .models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Ingredient
        fields = "__all__"





class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    #ingredients_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = "__all__"


    
    def create(self, validated_data):
        print("In Serializer Create")
        ingredients = validated_data.pop('ingredients')

        recipe = Recipe(**validated_data)
        recipe.save()
        for ingredient in ingredients:
            #new_ingredient = Ingredient.objects.create(**ingredient)
            recipe.ingredients.add(ingredient['id'])

        return recipe
    

    def update(self,instance, validated_data):
        
        instance.ingredients.clear()
        new_ingredients = validated_data.pop('ingredients')
        instance = super(RecipeSerializer, self).update(instance, validated_data)
        

        for ingredient in new_ingredients:
            old_ingredient = Ingredient.objects.get(pk=ingredient['id'])
            #old_ingredient.save()
            instance.ingredients.add(old_ingredient)
        
        instance.save()
        return instance