from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import BlogViewSet
from . import views

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
]
