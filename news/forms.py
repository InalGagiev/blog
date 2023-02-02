from .models import News
from django.forms import ModelForm, TextInput

class ArticlesFrom(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Называние статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Основной текст статьи'
            }),
        }