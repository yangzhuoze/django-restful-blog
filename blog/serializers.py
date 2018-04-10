from rest_framework import serializers

from blog.models import Article


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ('uid', 'title', 'body', 'body_raw', 'head_pic', 'created_time', 'modified_time', 'views_count')
