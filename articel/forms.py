from django import forms
from .models import *



class ArticleForm(forms.ModelForm):
    tags = forms.CharField(max_length=255)
    class Meta:
        model = Article
        fields = ['title', 'text', 'picture', 'tags']



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'user', 'photo']

    
class CommentsForm(forms.ModelForm):    
    class Meta:
        model = Comments
        fields = ['text'] 


