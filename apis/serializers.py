from rest_framework import serializers
from django.contrib.auth import get_user_model
from feed import models



class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'is_creator', 'is_adult')

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'website', 'biography', 'is_creator', 'is_adult', 'profile_pic')

class PostSerializer(serializers.ModelSerializer):
    comments = NestedCommentSerializer(many=True, read_only=True, source='details')
    posted_by = NestedUserSerializer(many=False, read_only=True, source='user_name')
    class Meta:
        model = models.Post
        fields = (
            'id',
            'comments',
            'user_name',
            'description',
            'pic',
            'date_posted',
            'posted_by',
            'tags',
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