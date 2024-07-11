from django.urls import path
from .views import BlogView,CommentView,LikeView

urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('comment/<int:pk>/',CommentView.as_view()),
    path('like/<int:pk>/',LikeView.as_view()),
] 