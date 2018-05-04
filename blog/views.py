from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

from blog.models import Article, Tag
from blog.serializers import ArticleSerializer, TagSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format)
    })


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


class TagViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
