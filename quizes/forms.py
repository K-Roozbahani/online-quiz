from django import forms
from .models import Option

from .models import Answer, Option


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['user', 'quiz', 'question', 'option']
