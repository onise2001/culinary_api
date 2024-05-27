from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .permissions import CanDelete, CanEdit
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS
from collections import Counter
from rest_framework.renderers import JSONRenderer
from .filters import RecommendationFilter
from decimal import Decimal
# Create your views here.




class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']

    def create(self, request, *args,**kwargs):
        for index,ingredient in enumerate(request.data['ingredients']):
               new_ing = Ingredient.objects.create(**ingredient)             
               request.data['ingredients'][index]['id'] = new_ing.id                                                                           

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            #print(serializer.validated_data)
            serializer.validated_data['user'] = request.user
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, *args, **kwargs ):
        item_ids = []
        for index,ingredient in enumerate(request.data['ingredients']):
            if 'id' not in ingredient.keys():
                new_ing = Ingredient.objects.create(**ingredient)
                request.data['ingredients'][index]['id'] = new_ing.id
            else:
                old_ing = Ingredient(pk=ingredient['id'], **ingredient)
                old_ing.save()
            item_ids.append(ingredient['id'])    
            
        instance = self.get_object()

        for ingredient in instance.ingredients.all():
            if ingredient.id not in item_ids: 
                Ingredient.objects.filter(pk=ingredient.id).delete()

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK, headers=headers)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    
    def get_permissions(self):

        if self.action in SAFE_METHODS:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        elif self.action == "create":
            self.permission_classes = [IsAuthenticated]

        elif self.action == "destroy":
            self.permission_classes = [CanDelete]
        elif self.action in ["update", "partial_update"]:
            self.permission_classes = [CanEdit]

        return [permission() for permission in self.permission_classes]    
            
    

  

class RecommendationViewSet(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [RecommendationFilter]
   

class RateRecipeViewSet(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        rating = Decimal(request.data.get('rating'))

        instance.rated_by += 1
        instance.all_rating +=  rating
        instance.average_rating = instance.all_rating / instance.rated_by
        serializer = RecipeSerializer(instance,data={'recipe': instance},partial=True )
        if serializer.is_valid():
            instance.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
