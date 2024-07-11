from django.shortcuts import render
from .models import Blog,Comment,Like
from .serializers import Blogserializers,Commentserializers,Likeserializers
from rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework import generics
from rest_framework import mixins

class BlogView(mixins.ListModelMixin,
               mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]

class LikeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]