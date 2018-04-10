from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from blog.models import Article
from blog.serializers import ArticleSerializer


@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        article = ArticleSerializer(data=data)
        if article.is_valid():
            article.save()
            return JsonResponse(article.data, status=201)
        return JsonResponse(article.errors, status=400)
