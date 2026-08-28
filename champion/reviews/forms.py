from django import forms
from .models import Reviews

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'name',
            'comment',
            'rating',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'create__name',
                'placeholder': 'имя',
            }),

            'comment': forms.Textarea(attrs={
                'class': 'create__comment',
                'placeholder': 'комментарий',
            }),

            'rating': forms.RadioSelect(
                choices = [(i, str(i)) for i in range(5, 0, -1)],
                attrs={
                    'class': 'create__rating-radio', # Добавляет класс к главному блоку
                }
            )
        }

    