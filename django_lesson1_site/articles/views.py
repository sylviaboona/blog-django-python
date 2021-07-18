from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm
from django.urls import reverse_lazy

# Create your views here.
class ArticlesCreate(CreateView):
    template_name = 'articles/article_form.html'
    model = Article
    form_class = ArticleForm
        
class ArticlesList(ListView):
    template_name = 'articles/articles.html'
    model = Article
    ordering = ['-id']

class ArticleDetail(DetailView):
    template_name = 'articles/article_details.html'
    model = Article

class UpdateArticle(UpdateView):
    template_name = 'articles/update_article.html'
    model = Article
    form_class = ArticleForm
    # fields = ['title', 'text']

class DeleteArticle(DeleteView):
    template_name = 'articles/delete_article.html'
    model = Article
    success_url = reverse_lazy('all-articles-url')


