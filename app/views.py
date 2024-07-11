from django.shortcuts import render
from .models import Blog,Comment,Like
from .serializers import Blogserializers,Commentserializers,Likeserializers
from rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework import generics
from rest_framework import mixins

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializers
    authentication_classes=[TokenAuthentication]

class BlogListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializers
    authentication_classes=[TokenAuthentication]

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]  

class CommentView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset=Comment.objects.all()
    serializer_class = Commentserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LikeListView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]  

class LikeView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Like.objects.filter(blog_id=self.kwargs['pk'])
        return queryset