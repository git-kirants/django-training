
from .views import BookingListView
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('admin/', admin.site.urls),
]
