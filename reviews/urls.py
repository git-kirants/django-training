
from .views import ReviewListView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('admin/', admin.site.urls),

]
