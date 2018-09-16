from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views
from blog.views import TagViewSet, ArticleViewSet, ConfigViewSet, UserViewSet, GroupViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})

group_list = GroupViewSet.as_view({
    'get': 'list',
})

config_list = ConfigViewSet.as_view({
    'get': 'list',
})

config_detail = ConfigViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

article_list = ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

article_detail = ArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

tag_list = TagViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

tag_detail = TagViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path(r'users/', user_list, name='users-list'),
    path(r'users/<pk>', user_detail, name='users-detail'),
    path(r'configs/', config_list, name='configs-list'),
    path(r'configs/<uid>/', config_detail, name='configs-detail'),
    path(r'articles/', article_list, name='article-list'),
    path(r'articles/<uid>/', article_detail, name='article-detail'),
    path(r'articles/<uid>/markdown/', views.ArticleMarkdown.as_view(), name='article-markdown'),
    path(r'tags/', tag_list, name='tag-list'),
    path(r'tags/<name>/', tag_detail, name='tag-detail'),
    path(r'', views.api_root, name='blog'),
])
