from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Interest, UserInterest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']  # name をフィールドに追加
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'name']

class UserInterestSerializer(serializers.ModelSerializer):
    interest = InterestSerializer()

    class Meta:
        model = UserInterest
        fields = ['id', 'user', 'interest']