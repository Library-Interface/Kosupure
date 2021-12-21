from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  ChatViewSet, CurrentChatView, CurrentUserView, UserViewSet, PostViewSet, CurrentPostView, CommentViewSet, CurrentCommentView, CurrentEventView, EventViewSet, EventsCommentsViewSet, CurrentEventsCommentsView, LiveViewSet, CurrentLiveView

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
router.register('events', EventViewSet, basename='events')
router.register('eventscomments', EventsCommentsViewSet, basename='eventscomments')
router.register('chat', ChatViewSet, basename='chat')
router.register('live', LiveViewSet, basename='live')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view()),
    path('currentpost/', CurrentPostView.as_view()),
    path('currentcomment/', CurrentCommentView.as_view()),
    path('currentevent/', CurrentEventView.as_view()),
    path('currenteventscomments/', CurrentEventsCommentsView.as_view()),
    path('currentchat/', CurrentChatView.as_view()),
    path('currentlive/', CurrentLiveView.as_view()),
]  