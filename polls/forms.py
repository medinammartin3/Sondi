from django import forms
from .models import Question, Choice


# --- FORMS FOR CREATE AND UPDATE POLLS ---

"""
Form for the question text and the visibility of the poll.
"""
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "visibility"]
        widgets = {
            'question_text': forms.TextInput(attrs={
                'placeholder': 'Enter your question'
            }),
            'visibility': forms.RadioSelect,
        }
        

"""
Form for the choices text
"""
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]
        labels = {"choice_text": "Choice"}

# Formset for display and manage multiple choice forms.
# Requires a minimum of 2 choices to create a new poll.
ChoiceFormSet = forms.modelformset_factory(
    Choice, fields=("choice_text",), extra=0, min_num=2, max_num=100, 
    error_messages = {
            'choice_text': {
                'required': '* Please enter a choice.',
            },
        },
    widgets = {
        'choice_text': forms.TextInput(attrs={
            'placeholder': 'Enter choice here'
        }),
    }
)



# --- FORMS FOR SEARCHING A POLL ---

"""
Form for searching a poll by its code.
"""
class CodeForm(forms.Form):
    question_code = forms.CharField(label=None, max_length=6, required=True, 
                                    widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter the question code'
                                        }),
                                    )
