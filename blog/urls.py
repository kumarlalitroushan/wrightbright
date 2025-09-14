from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import BlogViewSet
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_blog, name='create_blog'),
    path('myblogs/', views.my_blogs, name='my_blogs'),
    path('post/<int:id>/', views.full_blog_post, name='post-detail'),
    path('post/<int:id>/delete', views.post_delete_view, name='post-delete'),
    path('update/<int:id>/', views.post_update_view, name='post-update'),

    #password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'blog/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]