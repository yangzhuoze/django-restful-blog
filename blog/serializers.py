from rest_framework import serializers

from blog.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('uid', 'body', 'views_count')


class TagSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'articles')
