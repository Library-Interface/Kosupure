from rest_framework import generics, permissions, viewsets
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes

from .serializers import UserSerializer, PostSerializer, CommentSerializer
from feed import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'tags',
        'user_name__username',
    ]
    ordering_fields = '__all__'

class CurrentPostView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    def get_object(self):
        return self.request.user

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comments.objects.all()
    serializer_class = CommentSerializer
    def get_object(self):
        return self.request.user