from rest_framework import generics, permissions, viewsets
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from django_filters.rest_framework import DjangoFilterBackend

from apis.permissions import isCreatorOrReadOnly
from rest_framework import permissions
from .serializers import UserSerializer, PostSerializer, CommentSerializer, EventSerializer, EventsCommentsSerializer, ChatSerializer, LiveSerializer
from feed import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [isCreatorOrReadOnly]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = [
        'tags',
        'user_name__username',
        'details__comment',
        'description',
    ]
    ordering_fields = '__all__'
    filter_fields = [
        'tags',
        'user_name__username'
    ]
    permission_classes = [isCreatorOrReadOnly]

class CurrentPostView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    def get_object(self):
        return self.request.user

class CurrentCommentView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    def get_object(self):
        return self.request.user

class CurrentEventView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    def get_object(self):
        return self.request.user

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [isCreatorOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventsCommentsViewSet(viewsets.ModelViewSet):
    queryset = models.EventComments.objects.all()
    serializer_class = EventsCommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentEventsCommentsView(generics.RetrieveAPIView):
    serializer_class = EventsCommentsSerializer
    def get_object(self):
        return self.request.user

class CurrentChatView(generics.RetrieveAPIView):
    serializer_class = ChatSerializer
    def get_objects(self):
        return self.request.user

class ChatViewSet(viewsets.ModelViewSet):
    queryset = models.Chat.objects.all()
    serializer_class = ChatSerializer

class LiveViewSet(viewsets.ModelViewSet):
    queryset = models.Live.objects.all()
    serializer_class = LiveSerializer

class CurrentLiveView(generics.RetrieveAPIView):
    serializer_class = LiveSerializer
    def get_objects(self):
        return self.request.user