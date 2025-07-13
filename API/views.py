from django.shortcuts import render
from rest_framework import viewsets, permissions
from blog.models import Blog
from .serializer import BlogSerializer
from .permissions import OwnerOrAdmin

# Create your views here.

print(Blog.objects.all())

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_date')
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), OwnerOrAdmin()]
        elif self.action in ['create']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)