from django.urls import path
from .views import BlogView,CommentView,LikeView,CommentListView,LikeListView,BlogListView

urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('blog/<int:pk>/',BlogListView.as_view()),
    path('comment/<int:pk>/',CommentView.as_view()),
    path('comment/',CommentListView.as_view()),
    path('like/<int:pk>/',LikeView.as_view()),
    path('like/',LikeListView.as_view()),
] 