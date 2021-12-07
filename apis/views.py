from rest_framework import generics, permissions, viewsets
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user