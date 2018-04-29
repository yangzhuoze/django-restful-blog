from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = [
    path(r'articles/', views.ArticleList.as_view(), name='article-list'),
    path(r'articles/<uid>/', views.ArticleDetail.as_view(), name='article-detail'),
    path(r'articles/<uid>/markdown/', views.ArticleMarkdown.as_view(), name='article-markdown'),
    path(r'tags/', views.TagList.as_view(), name='tag-list'),
    path(r'tags/<name>/', views.TagDetail.as_view(), name='tag-detail'),
    path(r'', views.api_root, name='blog'),
]

urlpatterns = format_suffix_patterns(urlpatterns)