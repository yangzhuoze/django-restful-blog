from django.urls import path

from blog import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('', views.api_root, name='article-list'),
]