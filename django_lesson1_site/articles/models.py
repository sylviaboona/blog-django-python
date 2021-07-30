from django.urls import reverse
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all-articles-url')


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField(max_length=200, default = 'uncategorized')
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('all-articles-url')

    def get_article_title(self):
        return self.title

