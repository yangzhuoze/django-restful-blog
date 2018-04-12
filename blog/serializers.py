from rest_framework import serializers

from blog.models import Article
from common.utils.generate import uid_generate


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('uid', )

    def create(self, validated_data):
        article = Article(
            uid=uid_generate(),
            title=validated_data['title'], 
            body=validated_data['body'], 
            body_raw=validated_data['body_raw'], 
            head_pic=validated_data['head_pic'], 
            created_time=validated_data['created_time'], 
            modified_time=validated_data['modified_time'], 
            views_count=validated_data['views_count'], 
        )
        article.save()
        return article
