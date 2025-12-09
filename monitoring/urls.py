from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ScreenshotUploadView

urlpatterns = [
    # Login API (Desktop App এ এটি কল করবেন)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Screenshot Upload API
    path('api/upload-screenshot/', ScreenshotUploadView.as_view(), name='upload_screenshot'),
]