from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('author', 'email', 'text')
        labels = {
            'author': 'Автор записи',
            'email': 'Почта автора',
            'text': 'Текст'
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if len(author) < 2:
            raise ValidationError('Имя должно быть длинее 2-ух символов')
        return author