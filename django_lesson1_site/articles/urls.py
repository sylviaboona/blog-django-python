from django.urls import path
from articles.views import ArticlesCreate, ArticleDetail, ArticlesList, UpdateArticle, DeleteArticle


urlpatterns = [
    path('articles/', ArticlesCreate.as_view(), name='create-articles-url'), # our-domain.com/meetups
    path('list/', ArticlesList.as_view(), name='all-articles-url'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail-url'),
    path('article/edit/<int:pk>/', UpdateArticle.as_view(), name='update-article-url'),
    path('article/<int:pk>/delete/', DeleteArticle.as_view(), name='delete-article-url'),
]