from django.shortcuts import redirect, render
from rest_framework import viewsets, permissions
from .models import Blog
from .serializer import BlogSerializer
from .permissions import OwnerOrAdmin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import BlogForm
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    blog_list = Blog.objects.all().order_by('-created_date')
    paginator = Paginator(blog_list, 5)  # show 5 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'page_obj': page_obj})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # it will automatically log in the user after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('my_blogs')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog/my_blogs.html', {'blogs': blogs})

def full_blog_post(request, id):

    blog = Blog.objects.get(id=id)
    return render(request, 'blog/full_post.html', {'blog': blog})

@login_required
def post_delete_view(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        if request.user == blog.author or request.user.is_staff:
            blog.delete()
        return redirect('my_blogs')

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