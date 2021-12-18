from rest_framework import serializers
from django.contrib.auth import get_user_model
from feed import models



class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'is_creator', 'is_adult', 'id')

class NestedCommentSerializer(serializers.ModelSerializer):
    posted_by = NestedUserSerializer(many=False, read_only=True, source='user_name')
    class Meta:
        model = models.Comments
        fields = (
            'id',
            'post',
            'user_name',
            'comment',
            'comment_date',
            'posted_by',
        )

class NestedEventSerializer(serializers.ModelSerializer):
    event = NestedUserSerializer(many=False, read_only=True, source='events')
    class Meta:
        model = models.Events
        fields = (
            'event',
            'id', 
            'user', 
            'name', 
            'description', 
            'date',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'website', 'biography', 'is_creator', 'is_adult', 'profile_pic', 'likes', 'attending_events')

class PostSerializer(serializers.ModelSerializer):
    comments = NestedCommentSerializer(many=True, read_only=True, source='details')
    posted_by = NestedUserSerializer(many=False, read_only=True, source='user_name')
    liked_detail = NestedUserSerializer(many=True, read_only=True, source='liked_by')

    class Meta:
        model = models.Post
        fields = (
            'adult_content',
            'id',
            'comments',
            'user_name',
            'description',
            'pic',
            'date_posted',
            'posted_by',
            'tags',
            'liked_by',
            'liked_detail',
        )

class CommentSerializer(serializers.ModelSerializer):
    posted_by = NestedUserSerializer(many=False, read_only=True, source='user_name')
    class Meta:
        model = models.Comments
        fields = (
            'id',
            'post',
            'user_name',
            'posted_by',
            'comment_date',
            'comment',
        )

class EventsCommentsSerializer(serializers.ModelSerializer):
    event_username = NestedUserSerializer(many=False, read_only=True, source='events_user')
    class Meta:
        model = models.EventComments
        fields = (
            'id',
            'events',
            'events_user',
            'event_comment',
            'event_comment_date',
            'event_username'
        )

class EventSerializer(serializers.ModelSerializer):
    attending_details = NestedUserSerializer(many=True, read_only=True, source='attending')
    posted_by = NestedUserSerializer(many=False, read_only=True, source='user')
    comments = EventsCommentsSerializer(many=True, read_only=True, source='comment_events')
    class Meta:
        model = models.Events
        fields = (
            'id', 
            'comments',
            'user', 
            'name', 
            'description', 
            'date',
            'attending_details',
            'posted_by'
            )
        