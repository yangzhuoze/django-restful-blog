from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse

from blog.models import Article
from blog.serializers import ArticleSerializer


# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser.parse(request)
#         article = ArticleSerializer(data=data)
#         if article.is_valid():
#             article.save()
#             return JsonResponse(article.data, status=201)
#         return JsonResponse(article.errors, status=400)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list', request=request, format=format)
    })

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uid'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleMarkdown(generics.GenericAPIView):
    queryset = Article.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.body)
