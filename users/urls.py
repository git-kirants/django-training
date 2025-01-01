from django.urls import path
from .views import UserListView, CustomTokenObtainPairView, CustomTokenRefreshView

app_name = 'users'  # Add namespace

urlpatterns = [
    # Remove 'admin/' as it's handled in the main urls.py
    # Remove the empty include of 'backend.urls' to prevent circular reference
    path('', UserListView.as_view(), name='user-list'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
