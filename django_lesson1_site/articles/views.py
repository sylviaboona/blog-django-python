from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Article, Category
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AddCategory(LoginRequiredMixin, CreateView):
    template_name = 'articles/add_category.html'
    model = Category
    fields = '__all__'
    context_object_name = 'myarticles'

# Create your views here.
class ArticlesCreate(LoginRequiredMixin, CreateView):
    template_name = 'articles/article_form.html'
    model = Article
    form_class = ArticleForm
    # fields = ['title', 'text']

        
class ArticlesList(ListView):
    template_name = 'articles/articles.html'
    model = Article
    ordering = ['-id']
    context_object_name = 'myarticles'

class ArticleDetail(LoginRequiredMixin, DetailView):
    template_name = 'articles/article_details.html'
    model = Article

class UpdateArticle(LoginRequiredMixin, UpdateView):
    template_name = 'articles/update_article.html'
    model = Article
    form_class = ArticleForm
    # fields = ['title', 'text']

class DeleteArticle(LoginRequiredMixin, DeleteView):
    template_name = 'articles/delete_article.html'
    model = Article
    success_url = reverse_lazy('all-articles-url')

def category_view(request, cats):
    category_articles = Article.objects.filter(category=cats.replace('-',' '))

    return render(request, 'articles/categories.html', {'cats': cats.title().replace('-',' '), 'category_articles': category_articles,})
