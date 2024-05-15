from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from matching.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('matching.urls')),  # matching アプリの URL 設定をインクルード
]
