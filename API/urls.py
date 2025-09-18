from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, signup_api, password_reset_api, password_reset_confirm_api

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
path('api/', include(router.urls)),

# Authentication APIs
    path('api/auth/signup/', signup_api, name='api_signup'),
    path('api/auth/password-reset/', password_reset_api, name='api_password_reset'),
    path('api/auth/password-reset-confirm/', password_reset_confirm_api, name='api_password_reset_confirm'),
]
