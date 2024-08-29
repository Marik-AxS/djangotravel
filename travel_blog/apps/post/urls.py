from django.urls import path
from .views import *

urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post_details/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('post_detail/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
]