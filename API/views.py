from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from blog.models import Blog
from .serializer import BlogSerializer, SignupSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from .permissions import OwnerOrAdmin
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

print(Blog.objects.all())

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('created_date')
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), OwnerOrAdmin()]
        elif self.action in ['create']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    # API endpoint for user registration

    serializer = SignupSerializer(data = request.data)
    
    if serializer.is_valid():
        user = serializer.save()

    # Generating JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
                'message': 'User created successfully',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                'tokens': {
                    'access': access_token,
                    'refresh': refresh_token
                }
            }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_api(request):

    # API endpoint to request password reset

    serializer = PasswordResetSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        
        # Generate reset token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        # Create reset link (you might want to customize this URL)
        reset_link = f"{request.scheme}://{request.get_host()}/api/auth/password-reset-confirm/{uid}/{token}/"
        
        # Send email
        subject = 'Password Reset Request'
        message = f"""
        Hello {user.username},
        
        You requested a password reset for your account.
        Please click the link below to reset your password:
        
        {reset_link}
        
        If you didn't request this, please ignore this email.
        
        Best regards,
        WriteBright Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response({
                'message': 'Password reset email sent successfully.'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': 'Failed to send email. Please try again later.'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_confirm_api(request):
    
    # API endpoint to confirm password reset

    serializer = PasswordResetConfirmSerializer(data=request.data)
    if serializer.is_valid():
        uid = serializer.validated_data['uid']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']
        
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
            
            if default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                
                return Response({
                    'message': 'Password reset successful.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Invalid or expired token.'
                }, status=status.HTTP_400_BAD_REQUEST)
                
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({
                'error': 'Invalid reset link.'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
