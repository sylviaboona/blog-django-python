from django.test import TestCase
from articles.models import Article

# Create your tests here.
# Every test method must be prefixed with the word "test_"
class ArticleModelTest(TestCase):
    def test_get_article_title(self):
        """
        This method returns the name of the article
        """
        article = Article.objects.create(title='Mindset')
        self.assertEqual(article.get_article_title(), 'Mindset')
    
    def test_article_string_magic_method(self):
        """
        This method returns the string representation 
        """
        article = Article.objects.create(title='Mindset')
        self.assertEqual(str(article), 'Mindset')
