# ↓↓↓ Importeert het "Comment"-model uit models.py in deze directory
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
