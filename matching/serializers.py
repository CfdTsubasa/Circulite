from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User,Interest, UserInterest

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
        fields = ['id', 'name']  # レスポンスにnameを含める

class UserInterestSerializer(serializers.ModelSerializer):
    interest = serializers.PrimaryKeyRelatedField(queryset=Interest.objects.all(), many=False)

    class Meta:
        model = UserInterest
        fields = ['user', 'interest']

    def create(self, validated_data):
        interest = validated_data.pop('interest')
        user = validated_data.get('user')
        user_interest = UserInterest.objects.create(user=user, interest=interest)
        return user_interest