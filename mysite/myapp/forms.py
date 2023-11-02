from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['nickname', 'question_text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['nickname', 'answer_text']