from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/services/', include('services.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/community/', include('community.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/example/', views.example_api_view, name='example_api_view'),
]
