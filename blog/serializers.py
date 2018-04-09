from rest_framework import serializers

from .serializers import Article

class ArticleSerializer(serializers.Serializer):
    uid = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=128)
    body = serializers.CharField()
    body_raw = serializers.CharField()
    head_pic = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)
