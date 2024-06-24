from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterestViewSet, UserInterestViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'interests', InterestViewSet)
router.register(r'user-interests', UserInterestViewSet, basename='user-interests')

urlpatterns = [
    path('', include(router.urls)),  # ルーターのURLをインクルード
]
