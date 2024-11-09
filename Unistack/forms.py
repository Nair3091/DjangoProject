from django import forms
from .models import Post, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'code_snippet', 'code_file']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content','file']
