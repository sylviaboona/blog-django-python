from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Article
from .forms import ArticleForm

# Create your views here.
class ArticlesCreate(CreateView):
    template_name = 'articles/article_form.html'
    model = Article
    form_class = ArticleForm
        
class ArticlesList(ListView):
    template_name = 'articles/articles.html'
    model = Article

class ArticleDetail(DetailView):
    template_name = 'articles/article_details.html'
    model = Article

class UpdateArticle(UpdateView):
    template_name = 'articles/update_article.html'
    model = Article
    form_class = ArticleForm
    # fields = ['title', 'text']



