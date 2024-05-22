from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            #print(serializer.validated_data)
            serializer.validated_data['user'] = request.user
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, *args, **kwargs ):
        for ingredient in request.data['ingredients']:
            if 'id' not in ingredient.keys():
                ingredient = Ingredient.objects.create(**ingredient)
            
        instance = self.get_object()

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK, headers=headers)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
            

