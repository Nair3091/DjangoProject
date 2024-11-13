from django import forms
from .models import Post, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file']  # Ensure only existing fields are listed

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'file']  # Ensure only existing fields are listed
