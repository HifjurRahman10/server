from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True},
                        "email":{"required":True}}

    def validate_email(self, value):
        """
        Validate that the email is unique.
         """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ShortVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortVideo
        fields = ["userId","avatarId","hook","videoURL","created_at"] 