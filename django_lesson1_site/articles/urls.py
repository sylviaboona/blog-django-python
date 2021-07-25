from . import views
from django.urls import path
from articles.views import ArticlesCreate, ArticleDetail, ArticlesList, UpdateArticle, DeleteArticle, AddCategory

# app_name = 'articles'
urlpatterns = [
    path('articles/', ArticlesCreate.as_view(), name='create-articles-url'), # our-domain.com/meetups
    path('list/', ArticlesList.as_view(), name='all-articles-url'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail-url'),
    path('article/edit/<int:pk>/', UpdateArticle.as_view(), name='update-article-url'),
    path('article/<int:pk>/delete/', DeleteArticle.as_view(), name='delete-article-url'),
    path('addcategory/', AddCategory.as_view(), name='add-category-url'),
    path('category/<str:cats>/', views.category_view, name='articles-by-category')
]