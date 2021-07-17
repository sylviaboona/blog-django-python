from django import forms
from .models import Article
 
 
# creating a form
class ArticleForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Article
 
        # specify fields to be used
        fields = ( "title","text")
        
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'text': forms.Textarea(attrs = {'class': 'form-control'})
        }