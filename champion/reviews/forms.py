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
                'class': 'create__input',
                'plaсeholder': 'имя',
            }),

            'comment': forms.Textarea(attrs={
                'class': 'create__textarea',
                'plaсeholder': 'комментарий',
            }),

            'rating': forms.RadioSelect(
                choices = [(i, str(i)) for i in range(5, 0, -1)]
            )
        }

    