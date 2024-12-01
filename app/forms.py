from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Comment, Blog, Review

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'})
    )
    password = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    rating = forms.ChoiceField(label='Оценка сайта', choices=[(i, str(i)) for i in range(1, 6)])
    comments = forms.CharField(label='Комментарии', widget=forms.Textarea)
    subscribe = forms.BooleanField(label='Подписаться на новости', required=False)
    suggestions = forms.CharField(label='Предложения', widget=forms.Textarea, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'short_content', 'full_content', 'image', 'author')
        labels = {
            'title': 'Заголовок',
            'short_content': 'Краткое содержание',
            'full_content': 'Полное содержание',
            'image': 'Изображение',
            'author': 'Автор',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_content': forms.Textarea(attrs={'class': 'form-control'}),
            'full_content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['оценка', 'комментарий']
        labels = {
            'оценка': 'Оценка',
            'комментарий': 'Комментарий',
        }
        widgets = {
            'оценка': forms.Select(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'form-control'}),
            'комментарий': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
