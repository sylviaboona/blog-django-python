from django import forms
from .models import Article, Category
 
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)
# creating a form
class ArticleForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Article
 
        # specify fields to be used
        fields = ( "title", "category", "text")
        
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'text': forms.Textarea(attrs = {'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs = {'class': 'form-control'})
        }