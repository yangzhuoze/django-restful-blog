from rest_framework import serializers
from blog.models import Article, Tag


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all(), )
    url = serializers.HyperlinkedIdentityField(
        view_name='article-detail',
        lookup_field='uid'
    )

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('uid', 'body', 'views_count', 'tags')


class TagArticleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='article-detail',
        lookup_field='uid'
    )

    class Meta:
        model = Article
        fields = ('uid', 'title', 'url')


class TagSerializer(serializers.ModelSerializer):
    articles = TagArticleSerializer(many=True)

    class Meta:
        model = Tag
        depth = 1
        fields = '__all__'
        read_only_fields = ('articles_set',)
