from rest_framework import serializers
from .models import News, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'news', 'text', 'pub_date', 'is_hidden')

class NewsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'pub_date', 'is_hidden', 'comments')
