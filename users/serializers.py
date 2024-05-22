from rest_framework import serializers
from .models import CustomUser, Chef


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password",]
    

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ChefSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Chef
        fields = "__all__"

    
    def create(self, validated_data):
        user = validated_data.pop('user')
        password = user.pop('password')
        new_user = CustomUser(**user)
        new_user.set_password(password)
        new_user.save()
        chef = Chef(**validated_data)
        chef.user = new_user
        
        return chef
