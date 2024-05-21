from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer,InterestSerializer, UserInterestSerializer
from .models import User ,Interest,UserInterest
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)  # JWTトークンを生成
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class UserInterestViewSet(viewsets.ModelViewSet):
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_interest = serializer.save()  # 単一のUserInterestを保存
            response_data = UserInterestSerializer(user_interest).data  # 単一のUserInterestをシリアライズ
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print("Validation errors: ", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        print("test")
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserInterest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['delete'], url_path='delete-by-user-interest')
    def delete_by_user_and_interest(self, request):
        user_id = request.data.get('user')
        interest_id = request.data.get('interest')

        if not user_id or not interest_id:
            return Response({"detail": "User ID and Interest ID are required."}, status=status.HTTP_400_BAD_REQUEST)

        user_interests = UserInterest.objects.filter(user_id=user_id, interest_id=interest_id)
        
        if not user_interests.exists():
            return Response({"detail": "No matching UserInterest found."}, status=status.HTTP_404_NOT_FOUND)

        user_interests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user': {
            'id': self.user.id,
            'email': self.user.email
        }})
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer