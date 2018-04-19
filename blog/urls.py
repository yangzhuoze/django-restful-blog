from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = [
    path(r'articles/', views.ArticleList.as_view(), name='article-list'),
    path(r'articles/<uid>/', views.ArticleDetail.as_view(), name='article-detail'),
    path(r'', views.api_root, name='article-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)