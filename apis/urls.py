from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CurrentUserView, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view())
]