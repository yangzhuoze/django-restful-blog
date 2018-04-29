from rest_framework import serializers

from blog.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    # tags = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Tag.objects.all(), )
    tags = serializers.HyperlinkedRelatedField(
        view_name='tag-detail',
        queryset=Tag.objects.all(),
        many=True,
        allow_null=True,
        lookup_field='name'
    )

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('uid', 'body', 'views_count', 'tags')


class TagSerializer(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Tag
        fields = '__all__'
