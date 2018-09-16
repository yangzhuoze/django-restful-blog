from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

from blog.models import Article, Tag, Config
from blog.serializers import ArticleSerializer, TagSerializer, ArticleSimpleSerializer, ConfigSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format)
    })


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class ArticleMarkdown(generics.GenericAPIView):
    lookup_field = 'uid'
    queryset = Article.objects.all()
    renderer_classes = (StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.body)


class ArticleViewSet(viewsets.ModelViewSet):
    lookup_field = 'uid'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    simple_serializer_class = ArticleSimpleSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            if hasattr(self, 'simple_serializer_class'):
                return self.simple_serializer_class
        return super(ArticleViewSet, self).get_serializer_class()


class TagViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
