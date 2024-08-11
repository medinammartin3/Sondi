from typing import Text
from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]
        labels = {"question_text": "Question"}
        widgets = {
            'question_text': forms.TextInput(attrs={
                'placeholder': 'Enter your question'
            }),
        }
        

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]
        labels = {"choice_text": "Choice"}


ChoiceFormSet = forms.modelformset_factory(
    Choice, fields=("choice_text",), extra=1, min_num=2, max_num=100, 
    labels = {"choice_text": "Choice"},
    error_messages = {
            'choice_text': {
                'required': 'Please enter a choice.',
            },
        },
    widgets = {
        'choice_text': forms.TextInput(attrs={
            'placeholder': 'Enter choice here'
        }),
    }
)


class CodeForm(forms.Form):
    question_code = forms.CharField(label=None, max_length=5, required=True, 
                                    widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter the question code'
                                        }),
                                    )
    

# class VoteForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = []
#         choice = forms.ChoiceField(
#             choices=[],
#             widget=forms.RadioSelect
#         )

#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question', None)
#         super().__init__(*args, **kwargs)

#         if question:
#             choices = [(choice.id, choice.choice_text) for choice in question.choice_set.all()]
#             self.fields['choice'].choices = choices