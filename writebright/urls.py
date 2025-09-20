
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints
    path('api/', include('API.urls')),           # Blog APIs
    path('api/auth/', include('auth_API.urls')), # Authentication APIs
    
    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Web interface
    path('', include('blog.urls'))
]
