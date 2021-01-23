from django import forms

from .models import Recall


class RecallForm(forms.ModelForm):

    class Meta:
        model = Recall
        fields = ['title', 'text', ]
        labels = {'title': 'Заголовок',
                  'text': 'Отзыв',
                  }

        widgets = {
            'title': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв', 'rows': '15'}),
        }
