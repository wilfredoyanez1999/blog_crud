from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-new")
]
