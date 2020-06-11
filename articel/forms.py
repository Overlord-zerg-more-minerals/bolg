from django import forms
from .models import *


class ArticleForm(form.ModelForm):
    class Meta:
        model = ArticleForm
        fields = ['title', 'text', 'author']

class authorForm(forms.ModelForm):
    