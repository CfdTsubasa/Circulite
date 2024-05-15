from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterestViewSet, UserInterestViewSet

router = DefaultRouter()
router.register(r'interests', InterestViewSet)
router.register(r'user-interests', UserInterestViewSet)

urlpatterns = [
    path('', include(router.urls)),  # ルーターのURLをインクルード
]
