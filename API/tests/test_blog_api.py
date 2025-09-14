# import pytest
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from blog.models import Blog


# @pytest.fixture
# def api_client():
#     return APIClient()

# @pytest.fixture
# def create_user(db):
#     def make_user(username, password='pass123'):
#         user = User.objects.create_user(username=username, password=password)
#         return user, password
#     return make_user

# @pytest.fixture
# def get_jwt_token(api_client, create_user):
#     user, password = create_user('testuser')
#     response = api_client.post('/api/token/', {'username': user.username, 'password': password})
#     assert response.status_code == 200
#     token = response.data['access']
#     return token, user