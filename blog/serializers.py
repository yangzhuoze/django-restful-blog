from rest_framework import serializers
from blog.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all(), )
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='article-detail',
    #     lookup_field='uid'
    # )

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('uid', 'title', 'created_time', 'tags')
        read_only_fields = ('uid', 'body', 'views_count', 'tags')


class TagArticleSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='article-detail',
    #     lookup_field='uid'
    # )

    class Meta:
        model = Article
        fields = ('title', 'uid')


class TagSerializer(serializers.ModelSerializer):
    articles = TagArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('name', 'articles')
