from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

from blog.models import Article, Tag
from blog.serializers import ArticleSerializer, TagSerializer
from common.utils.renderers import MarkdownRenderer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format)
    })


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uid'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleMarkdown(generics.GenericAPIView):
    lookup_field = 'uid'
    queryset = Article.objects.all()
    renderer_classes = (StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.body)


class TagList(generics.ListCreateAPIView):
    lookup_field = 'name'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
