from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_api, name='auth_signup'),
    path('password-reset/', views.password_reset_api, name='auth_password_reset'),
    path('password-reset-confirm/', views.password_reset_confirm_api, name='auth_password_reset_confirm'),
]