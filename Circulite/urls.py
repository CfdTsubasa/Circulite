from django.contrib import admin
from django.urls import path, include
from matching.views import CustomTokenObtainPairView  # アプリ名に応じて適宜変更
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('matching.urls')),  # アプリのurlsを含める
]
