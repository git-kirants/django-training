from django.urls import path
from . import views

app_name = 'services'  # Unique namespace

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service-list'),
    # Add other service-related paths here
]
