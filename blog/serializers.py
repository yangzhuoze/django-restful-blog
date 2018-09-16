from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Article, Tag, Config


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'


class ArticleSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('uid', 'title', 'created_time')
        read_only_fields = ('uid', 'title', 'created_time')


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all(), )
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='article-detail',
    #     lookup_field='uid'
    # )

    class Meta:
        model = Article
        fields = '__all__'
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
