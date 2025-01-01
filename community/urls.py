
from .views import PostListView, CommentListView
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('admin/', admin.site.urls),

]
