from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea,  ClearableFileInput

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title','anons', 'full_text', 'img']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }),

        }
